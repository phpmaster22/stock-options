from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView
import datetime
from option.models import Option, Times
import threading
import pandas as pd
import sqlite3
from datetime import datetime as date


def f():
    connection = sqlite3.connect('db.sqlite3')
    cursor = connection.cursor()

    sector_detail = pd.read_csv("symbols.csv")

    url_call = "https://www.moneycontrol.com/stocks/fno/marketstats/options/active_calls/homebody.php"
    url_put = "https://www.moneycontrol.com/stocks/fno/marketstats/options/active_puts/homebody.php"

    df_list_call = pd.read_html(url_call)
    df_call = df_list_call[0]
    df_call.columns = df_call.columns.str.replace(' ', '')

    df_list_put = pd.read_html(url_put)
    df_put = df_list_put[0]
    df_put.columns = df_put.columns.str.replace(' ', '')

    df = pd.concat([df_put, df_call], ignore_index=True)
    del df["Shares"], df["Contracts"]
    df.columns = ["symbol", "expiry", "option_type", "strike_price", "last_price", "price_change",
                  "high_low_price", "option_value", "open_interest", "open_interest_change"]
    pcp = df["price_change"].str.split(" ")
    df["price_change"] = [float(i[0].replace(",", '').replace("%", '')) for i in pcp]
    df["price_change_perc"] = [float(i[1].replace(",", '').replace("%", '')) for i in pcp]

    oic = df["open_interest_change"].str.split(" ")
    df["open_interest_change"] = [float(i[0].replace(",", '').replace("%", '')) for i in oic]
    df["open_interest_change_perc"] = [float(i[1].replace(",", '').replace("%", '')) for i in oic]

    hlp = df["high_low_price"].str.split(" ")
    df["high"] = [float(i[0].replace(",", '').replace("%", '')) for i in hlp]
    df["low"] = [float(i[1].replace(",", '').replace("%", '')) for i in hlp]
    del df["high_low_price"]

    fdf = pd.merge(df, sector_detail, on=["symbol"], how="left")
    fdf = fdf.reindex(
        ["symbol", "sector", "expiry", "option_type", "strike_price", "last_price", "price_change", "price_change_perc",
         "high", "low", "option_value", "open_interest", "open_interest_change", "open_interest_change_perc"], axis=1)

    fdf.loc[(fdf['price_change_perc'] > 0) & (fdf['open_interest_change_perc'] > 0), 'stock_position'] = 'buying'
    fdf.loc[(fdf['price_change_perc'] < 0) & (fdf['open_interest_change_perc'] < 0), 'stock_position'] = 'long_cover'
    fdf.loc[(fdf['price_change_perc'] < 0) & (fdf['open_interest_change_perc'] > 0), 'stock_position'] = 'writing'
    fdf.loc[(fdf['price_change_perc'] > 0) & (fdf['open_interest_change_perc'] < 0), 'stock_position'] = 'short_cover'

    cursor.execute("DELETE from option_option")
    fdf.to_sql("option_option", connection, if_exists='append', index=False)
    connection.close()

    Times.objects.filter(active=True).update(active=False)
    Times.objects.create(last_update=datetime.datetime.now(), active=True)
    t1 = threading.Thread(target=f)
    t1.start()


if date.today().strftime("%A") not in ["Sunday", "Saturday"]:
    t1 = threading.Thread(target=f)
    t1.start()


class Options(TemplateView):
    def get(self, request, *args, **kwargs):
        date_detail = Times.objects.filter(active=True).values("last_update")
        if date_detail:
            date_detail = date_detail[0]
        else:
            date_detail = ""
        all_data = Option.objects.filter(option_value__gte=0).order_by('-option_value').values()
        ce_buying = Option.objects.filter(option_type="CE", stock_position="buying").values("option_value")
        ce_writing = Option.objects.filter(option_type="CE", stock_position="writing").values("option_value")
        ce_long_cover = Option.objects.filter(option_type="CE", stock_position="long_cover").values("option_value")
        ce_short_cover = Option.objects.filter(option_type="CE", stock_position="short_cover").values("option_value")
        pe_buying = Option.objects.filter(option_type="PE", stock_position="buying").values("option_value")
        pe_writing = Option.objects.filter(option_type="PE", stock_position="writing").values("option_value")
        pe_long_cover = Option.objects.filter(option_type="PE", stock_position="long_cover").values("option_value")
        pe_short_cover = Option.objects.filter(option_type="PE", stock_position='short_cover').values("option_value")

        cbv = round(float(sum([a['option_value'] for a in ce_buying])), 1)
        cwv = round(float(sum([b['option_value'] for b in ce_writing])), 1)
        clv = round(float(sum([c['option_value'] for c in ce_long_cover])), 1)
        csv = round(float(sum([d['option_value'] for d in ce_short_cover])), 1)
        pbv = round(float(sum([e['option_value'] for e in pe_buying])), 1)
        pwv = round(float(sum([f['option_value'] for f in pe_writing])), 1)
        plv = round(float(sum([g['option_value'] for g in pe_long_cover])), 1)
        psv = round(float(sum([h['option_value'] for h in pe_short_cover])), 1)

        bullish = len(ce_buying) + len(ce_short_cover) + len(pe_writing) + len(pe_long_cover)
        bearish = len(ce_writing) + len(ce_long_cover) + len(pe_buying) + len(pe_short_cover)
        bullish_value = cbv + csv + pwv + plv
        bearish_value = cwv + clv + pbv + psv

        # Sector details...
        bullish_data = Option.objects.filter(Q(option_type="CE", stock_position="buying") |
                                             Q(option_type="CE", stock_position="short_cover") |
                                             Q(option_type="PE", stock_position="writing") |
                                             Q(option_type="PE", stock_position="long_cover")
                                             )
        bearish_data = Option.objects.filter(Q(option_type="CE", stock_position="writing") |
                                             Q(option_type="CE", stock_position="long_cover") |
                                             Q(option_type="PE", stock_position="buying") |
                                             Q(option_type="PE", stock_position="short_cover")
                                             )
        sector_detail = [i["sector"] for i in Option.objects.values("sector").distinct()]
        detail_list = []
        for s in sector_detail:
            bullish_data_s = bullish_data.filter(sector=s)

            no_stocks = len([s["symbol"] for s in bullish_data_s.values("symbol").distinct()])
            bullishness = [i["option_value"] for i in bullish_data_s.values()]

            all_s = Option.objects.values()
            alls = [a["option_value"] for a in all_s.filter(sector=s)]
            all_money = sum([a["option_value"] for a in all_s])

            sentiments = round(float((len(bullishness) / len(alls)) * 100), 1)
            buy_sell_value = round(float((sum(bullishness) / sum(alls)) * 100), 1)
            total_money = round(float(sum(alls)), 1)
            total_money_per = round(float((total_money / all_money) * 100), 1)
            detail_list.append({"sectors": s, "stocks": no_stocks, "sentiments": sentiments, "buy_sell": buy_sell_value,
                                "total_money": total_money,
                                "total_money_per": total_money_per})

        try: bulls = round(float((bullish / (bullish + bearish)) * 100), 1)
        except Exception: bulls = 0
        try: brs = round(float((bearish / (bullish + bearish)) * 100), 1)
        except Exception: brs = 0
        try: bulv = round(float((bullish_value / (bullish_value + bearish_value)) * 100), 1)
        except Exception: bulv = 0
        try: brsv = round(float((bearish_value / (bullish_value + bearish_value)) * 100), 1)
        except Exception: brsv = 0

        return render(request, "index.html", context={
            "date_detail": date_detail,
            "sector_detail": detail_list,
            "option_data": all_data,
            'ce_buying': len(ce_buying),
            "ce_writing": len(ce_writing),
            "ce_long_cover": len(ce_long_cover),
            "ce_short_cover": len(ce_short_cover),
            "pe_buying": len(pe_buying),
            "pe_writing": len(pe_writing),
            "pe_long_cover": len(pe_long_cover),
            "pe_short_cover": len(pe_short_cover),
            "bull": bulls,
            "bear": brs,
            "ce_buying_value": cbv,
            "ce_writing_value": cwv,
            "ce_long_value": clv,
            "ce_short_value": csv,
            "pe_buying_value": pbv,
            "pe_writing_value": pwv,
            "pe_long_value": plv,
            "pe_short_value": psv,
            "bull_value": bulv ,
            "bear_value": brsv

        })
