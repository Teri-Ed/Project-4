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
    if request.method == 'POST':
        ticker = request.POST['ticker']
        #pk_c9d8aa3cdbc143dc9af6fe0d62e7d6d4
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_c9d8aa3cdbc143dc9af6fe0d62e7d6d4")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
        return render(request, 'main.html', {'api': api}) 
    else:
        return render(request, 'main.html', {'ticker': "Enter a ticker symbol to get your quote."})

def sell_stock(request):
    return render(request, 'about.html', {})

def about(request):
    return render(request, 'about.html', {})

def buy_stock(request):
    if request.method == 'GET':
        form = BuyStock()
        stocks = BuyStockModel.objects.all().order_by('-created')
        output = {'form' : form, 'stocks' : stocks}
        #money = 0
        #avail_money = Bank.objects.values('account')
        #cost = BuyStockModel.objects.values('total_value')
        #money += avail_money - cost
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

"""
def stock_market(request):
    if request.method == 'GET':
        form = BuyStock()
        stocks = BuyStockModel.objects.all().order_by('-created')
        output = {'form' : form, 'stocks' : stocks}
        stock_ticker = Stock.objects.all()
        api_output = []
        for ticker_item in ticker:
            api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=pk_c9d8aa3cdbc143dc9af6fe0d62e7d6d4")
            try:
                api = json.loads(api_request.content)
                api_output.append(api)
            except Exception as e:
               api = "Error..."
        return render(request, 'stock_market.html', 'stock_ticker' : stock_ticker, 'api_output' : api_output, output)

    elif request.method == 'POST': 
        form = BuyStock(request.POST or None)
        api_form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            form = BuyStock()
            return redirect('stock_market')
         
        if api_form.is_valid():
            api_form.save()
            messages.success(request, ("Stock Has Been Added"))
            return redirect('stock_market')
        return render(request, 'stock_market', {'form' : form, 'name' : name, 'price' : price, 'quantity' : quantity})
"""

def add_stock(request):
    import requests 
    import json

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

#def delete(request, stock_id):
#   item = Stock.objects.get(pk = stock_id)
#    item.delete()
#    messages.success(request, ("Stock Has Been Deleted"))
#    return redirect(add_stock)