from django.urls import path

urlpatterns = [
    # path('/', include("future.urls")),
]

# https://www.nseindia.com/api/option-chain-equities?symbol=AARTIIND

# Option details




# https://www.nseindia.com/api/quote-equity?symbol=AARTIIND
# current price



# https://www.nseindia.com/api/historical/cm/equity?symbol=AARTIIND&series=[%22AF%22,%22BE%22,%22BL%22,%22EQ%22]&from=30-09-2022&to=31-10-2022
# time series data.....


# option_data = requests.get("https://www.nseindia.com/api/option-chain-equities?symbol=AARTIIND",
#                            headers=request_header)
# return JsonResponse(option_data.json())
# https://www.nseindia.com/api/quote-derivative?symbol=AARTIIND