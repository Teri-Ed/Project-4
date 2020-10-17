from django.shortcuts import render, redirect
from .models import Stock, Bank, BuyStockModel
from .forms import StockForm, BankForm, BuyStock, Registration
from django.contrib import messages
import requests 
import json

def register(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect('login/')
    else:
        form = Registration()
        return render(request, 'register.html', {"form" : form})

def main(request):
    stocks = BuyStockModel.objects.all().order_by('-created')
    form = BuyStock()
    if request.method == 'POST':
        ticker = request.POST['ticker']
        #pk_c9d8aa3cdbc143dc9af6fe0d62e7d6d4
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_c9d8aa3cdbc143dc9af6fe0d62e7d6d4")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
        context = {'api': api, 'form' : form, 'stocks' : stocks}
        return render(request, 'buy_stock.html', context)
    else:
        context = {'form' : form, 'stocks' : stocks}
        return render(request, 'buy_stock.html', context)

def sell_stock(request):
    return render(request, 'about.html', {})

def about(request):
    return render(request, 'about.html', {})

def buy_stock(request):
    print('buy_stock')
    if request.method == 'GET':
        form = BuyStock()
        stocks = BuyStockModel.objects.all().order_by('-created')
        output = {'form' : form, 'stocks' : stocks}
        return render(request, 'buy_stock.html', output)

    elif request.method == 'POST': 
        form = BuyStock(request.POST or None)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity'] 
            form = BuyStock()
            return redirect('buy_stock')
        return render(request, 'buy_stock.html', {'form' : form, 'name' : name, 'price' : price, 'quantity' : quantity})

def sell_stock(request, stock_id):
    item = BuyStockModel.objects.get(pk = stock_id)
    item.delete()
    messages.success(request, ("Stock Has Been Deleted"))
    return redirect(buy_stock)

def add_stock(request):
    if request.method == 'POST':
        form = StockForm(request.POST or None)
         
        if form.is_valid():
            form.save()
            messages.success(request, ("Stock Has Been Added"))
            return redirect('add_stock')
   
    else:
        ticker = Stock.objects.all()
        output = []
        for ticker_item in ticker:
            api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=pk_c9d8aa3cdbc143dc9af6fe0d62e7d6d4")
            try:
                api = json.loads(api_request.content)
                output.append(api)
            except Exception as e:
               api = "Error..."
        return render(request, 'add_stock.html', {'ticker': ticker, 'output' : output})
