from django.shortcuts import render

def home(request):
    import requests 
    import json

    #pk_c9d8aa3cdbc143dc9af6fe0d62e7d6d4
    api_request = requests.get("https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_c9d8aa3cdbc143dc9af6fe0d62e7d6d4")

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."


    return render(request, 'home.html', {'api': api})

def about(request):
    return render(request, 'about.html', {})
