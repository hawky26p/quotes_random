from django.shortcuts import render

# Create your views here.

import requests

def home(request):
    return render(request, 'quotes/home.html')

def quote_list(request):
    try:
        response = requests.get('https://api.quotable.io/quotes/random')
        response.raise_for_status() 
        quotes_fetched = response.json()
    except requests.RequestException as e:
       
        error_message = f"Error fetching quotes: {e}"
        quotes_fetched = []  
    return render(request, 'website.html', {'quotes': quotes_fetched})