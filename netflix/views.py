from django.shortcuts import render
from django.conf import settings
import requests
from django.contrib.auth import authenticate, logout
from .forms import registerUserForm

# Create your views here.
def index(request):
  title = 'Netflix clone Homepage'
  url = (settings.API_LINK).format(type = 'movie', search_term = 'popular', api_key = settings.API_KEY)
  results_returned = requests.get(url).json()

  #returning now playing category
  url = (settings.API_LINK).format(type = 'movie', search_term = 'top_rated', api_key = settings.API_KEY)
  results_returned2 = requests.get(url).json()

  context = {
      'results':results_returned['results'][0:12],
      'top_rated':results_returned2['results'][0:6],
      'title':title,
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
    title = results_returned['original_title']
    context = {
      'results':results_returned,
      'movie_title':title
    }

    return render(request, 'search_results.html',context)

def register_user(request):
  '''
  Registers a user using to application, redirects to homepage
  '''
  form = registerUserForm
  title = 'Register - Movie Slack'



  context = {
    'title':title,
    'form':form,
  }

  return render(request, 'register_login.html', context)

def login_user(request):
  '''
  Logs in a registered user to the application, redirects to homepage
  '''
  title = 'Login-Movie Slack'


  context = {
    'title':title
  }
  return render(request, 'register_login.html', context)


def logout_user(request):
  '''
  Logs out a logged in user out of the apllication, redirects to login page
  '''
  title = 'Logout - Movie Slack'
  logout()
  context = {
    'title':title
  }