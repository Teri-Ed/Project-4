from django.contrib import admin
from .models import Stock, Bank, BuyStockModel

admin.site.register(Stock)
admin.site.register(Bank)
admin.site.register(BuyStockModel)