from django import forms
from .models import Stock, Bank, BuyStockModel

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ["ticker"]

class BankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = ["account"]

class BuyStock(forms.ModelForm):
    class Meta:
        model = BuyStockModel
        fields = ["name", "price", "quantity"]

        widgets = {
            'name' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'price' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'quantity' : forms.TextInput(attrs = {'class' : 'form-control'}),
        }


