from django.shortcuts import render
from django.conf import settings
import requests

# Create your views here.
def index(request):
  title = 'Netflix clone Homepage'
  results_returned = {}

  link = 'https://api.themoviedb.org/3/{type}/{search_term}?api_key={api_key}&language=en-US&page=1'
  apikey = settings.API_KEY
  url = link.format(type = 'movie', search_term = 'popular', api_key = apikey)
  movie_results = requests.get(url)
  results_returned = movie_results.json()
  results_returned['success'] = True
  context = {
      'results':results_returned['results'],
      'title':title
    }

  return render(request, 'index.html', context)

def search_movies(request):
  
  if 'search_movie' in request.GET and request.GET['search_movie']:
    search_trm= request.GET.get('search_movie')
    link = 'https://api.themoviedb.org/3/{type}/{search_term}?api_key={api_key}&language=en-US&page=1'
    apikey = settings.API_KEY
    url = link.format(type = 'movie', search_term = search_trm, api_key = apikey)
    results = requests.get(url)
    results_returned = results.json()
    print(url)
    title = results_returned['original_title']
    context = {
      'results':results_returned,
      'movie_title':title
    }

    return render(request, 'search_results.html',context)