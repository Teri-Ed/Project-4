from django.db import models 

class Stock(models.Model):
    ticker = models.CharField(max_length = 10)

    def __str__(self):
        return self.ticker

class Bank(models.Model):
    money = models.CharField(max_length = 10)

    def __str__(self):
        return self.money

class BuyStockModel(models.Model):
    name = models.CharField(max_length = 100)
    price = models.FloatField()
    quantity = models.IntegerField()
    created = models.DateTimeField(auto_now_add = True)

