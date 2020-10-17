from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name = "main"),
    path('register.html', views.register, name = "register"),
    #path('login.html', views.login, name = "login"),
    path('sell_stock', views.sell_stock, name = "sell_stock"),
    path('about.html', views.about, name = "about"),
    #path('stock_market.html', views.stock_market, name = "stock_market"),
    path('buy_stock.html', views.buy_stock, name = "buy_stock"),
    path('sell_stock/<stock_id>', views.sell_stock, name = "sell_stock"),
    path('add_stock.html', views.add_stock, name = "add_stock"),
    #path('delete/<stock_id>', views.delete, name = "delete"),
]