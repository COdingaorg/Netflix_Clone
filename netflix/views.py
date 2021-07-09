from django.shortcuts import render
from netflix_clone import settings
import requests

# Create your views here.
def index(request):
  title = 'Netflic clone Homepage'

  return render(request, 'index.html', {'title':title})

def search_movies(request):
  
  if 'search_movie' in request.GET and request.GET['search_movie']:
    search_term = request.GET.get('search_movie')
    link = settings.API_LINK
    api_key = settings.API_KEY
    url = link.format(type = 'movie', search_term = search_term, api_key = api_key)
    results = requests.get(url)

    context = {
      'results':results
    }
    
    return render(request, context)