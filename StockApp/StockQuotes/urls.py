from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name = "main"),
    path('register', views.register, name = "register"),
    path('sell_stock', views.sell_stock, name = "sell_stock"),
    path('about.html', views.about, name = "about"),
    path('buy_stock.html', views.buy_stock, name = "buy_stock"),
    path('sell_stock/<stock_id>', views.sell_stock, name = "sell_stock"),
    path('add_stock.html', views.add_stock, name = "add_stock"),
]