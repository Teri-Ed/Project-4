from django import forms
from .models import Stock, Bank, BuyStockModel
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Registration(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

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


