from django.shortcuts import render
from django.conf import settings
import requests

# Create your views here.
def index(request):
  title = 'Netflix clone Homepage'
  results_returned = {}

  link = settings.API_LINK
  apikey = settings.API_KEY
  url = link.format(type = 'movie', search_term = 'popular', api_key = apikey)
  movie_results = requests.get(url)
  if movie_results.status_code==200:
    results_returned = movie_results.json()
    results_returned['success'] = True
  else:
    results_returned['success'] = False
    if results_returned.status_code == 400:
      results_returned['message'] = 'No Movies Found'
    
    else:
      results_returned['message'] = 'Movies are Not available at the moment'
  
    movie_title = results_returned['original_title']
    context = {
      'results':results_returned,
      'movie_title':movie_title,
      'title':title
    }

    return render(request, 'index.html', context)

def search_movies(request):
  
  if 'search_movie' in request.GET and request.GET['search_movie']:
    search_trm= request.GET.get('search_movie')
    link = settings.API_LINK
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