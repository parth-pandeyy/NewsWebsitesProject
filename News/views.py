from django.shortcuts import render
API_KEY = '2be644d283e44a0ba44b2a4a3a4b5aef'
# Create your views here.
import requests
def index(request):
    url = f'https://newsapi.org/v2/top-headlines?country=in&apiKey=2be644d283e44a0ba44b2a4a3a4b5aef'
    data = requests.get(url)
    response = data.json()
    articles = response['articles']
    context={'articles':articles}
    return render(request,'index.html',context)

def category(request,name):
    url = f'https://newsapi.org/v2/top-headlines?category={name}&apiKey=2be644d283e44a0ba44b2a4a3a4b5aef'
    data = requests.get(url)
    response = data.json()
    articles = response['articles']
    context = {'articles':articles, 'category':name}
     return render(request,'category.html',context)

def search(request):
    search_term = request.GET['search']
    url = f'https://newsapi.org/v2/everything?q={search_term}&apiKey=2be644d283e44a0ba44b2a4a3a4b5aef'
    data = requests.get(url)
    response = data.json()
    articles = response['articles']
    context = {'articles':articles, 'search':search_term}
    return render(request,'search.html',context)
