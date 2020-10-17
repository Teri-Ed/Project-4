from django.db import models 

class Stock(models.Model):
    ticker = models.CharField(max_length = 10)

    def __str__(self):
        return self.ticker

class Bank(models.Model):
    account = models.DecimalField(max_digits = 15, default = 30000.0, decimal_places = 0, editable = True)

class BuyStockModel(models.Model):
    name = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits = 15, decimal_places = 2)
    quantity = models.DecimalField(max_digits = 15, decimal_places = 0)
    total_value = models.DecimalField(max_digits = 15, default = 1, decimal_places = 0, editable = True)
    created = models.DateTimeField(auto_now_add = True)

    def calc_total(self):
        amount = (self.price * self.quantity)
        return amount

    def save_total(self):
        self.total_value = self.calc_total()
        super(BuyStockModel, self).save()
