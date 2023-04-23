from django.shortcuts import render
import requests
# Create your views here.
def homepage(request):
    country = request.GET.get('country')
    category = request.GET.get('category')
    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey=ca86407e7be949aba091db60b69ea959'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    if category:
        url = f'https://newsapi.org/v2/top-headlines?category={category}&country=in&apiKey=ca86407e7be949aba091db60b69ea959'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    
    context = {
        'articles' : articles
    }

    return render(request,'homepage.html',context)