from django.db import models
from django.utils.datetime_safe import datetime


# Create your models here.


class Option(models.Model):
    symbol = models.CharField(max_length=50)
    sector = models.CharField(max_length=50)
    expiry = models.CharField(null=True, max_length=50)
    option_type = models.CharField(choices=[('CE', 'CE'), ('PE', 'PE')], max_length=10)
    strike_price = models.FloatField(null=True)
    last_price = models.FloatField(null=True)
    price_change = models.FloatField(null=True)
    price_change_perc = models.FloatField(null=True)
    high = models.FloatField(null=True)
    low = models.FloatField(null=True)
    option_value = models.FloatField(default=0.0)
    open_interest = models.FloatField(null=True)
    open_interest_change = models.FloatField(null=True)
    open_interest_change_perc = models.FloatField(null=True)
    stock_position = models.CharField(max_length=20, null=True)

    # price_change_perc > 0 and open_interest_change_perc > 0 Buying True
    # price_change_perc < 0 and open_interest_change_perc < 0 Long Cover True
    # price_change_perc < 0 and open_interest_change_perc > 0 Writing True
    # price_change_perc > 0 and open_interest_change_perc < 0 Short Cover True



class Times(models.Model):
    last_update = models.DateTimeField(null=True)
    active = models.BooleanField(default=False)
