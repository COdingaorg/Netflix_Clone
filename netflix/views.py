from netflix.models import UserProfile
from django.shortcuts import redirect, render
from django.conf import settings
import requests
from django.contrib.auth import authenticate, logout, login
from .forms import registerUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from decouple import config,Csv
from googleapiclient.discovery import build
import requests,json
from .forms import add_profile_form

#API KEYS and Request Parameters
 
YOUTUBE =  config('YOUTUBE_API_KEY') 

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
  if request.user.is_authenticated:
    return redirect('home')
  else:
    if request.method == 'POST':
      form = registerUserForm(request.POST)
      if form.is_valid(): 
        form.save()
        messages.success(request, 'Account Created Successfully')
        return redirect('login')

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
  if request.user.is_authenticated:
    return redirect('home')
  else:
    if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('password')
      user = authenticate(request, username = username, password = password)

      if user is not None:
        login(request, user)

        return redirect('home')

      else:
        messages.warning(request, 'Username or password is Incorrect')
        return redirect('login')
  
    context = {
      'title':title
    }
    return render(request, 'login.html', context)

@login_required(login_url='login')
def logout_user(request):
  '''
  Logs out a logged in user out of the apllication, redirects to login page
  '''
  logout(request)
  
  return redirect('login')

@login_required(login_url='login')
def add_user_profile(request):
  '''
  View function to add user profile
  '''

  try:
    user_profile = UserProfile.objects.filter(user = request.user).first()
  except UserProfile.DoesNotExist:
    user_profile = None

  form = add_profile_form
  if request.method == 'POST':
    form = add_profile_form(request.POST, request.FILES)
    if form.is_valid():
      new_profile = form.save(commit=False)
      new_profile.user = request.user
      new_profile.save()
    else:
      messages.warning(request, 'invalid data added')

  context = {
    'form':form,
    'user_profile':user_profile,
    'title':f'{request.user.username}\'s Profile'
  }

  return render(request, 'user_profile.html', context)
# Create your views here.
# def movies(request):
#     popular_movies_tmdb = tmdb.Movies('popular')
#     popular_movies = popular_movies_tmdb.info()['results']

#     upcoming_movies_tmdb = tmdb.Movies('upcoming')
#     upcoming_movies = upcoming_movies_tmdb.info()['results']

#     # nowshowing_movies_tmdb = tmdb.Movies('nowshowing')
#     # nowshowing_movies = nowshowing_movies_tmdb.info()['results']

#     return render(request, 'index.html', {'popular':popular_movies, 'upcoming':upcoming_movies})



# def youtube_movie(request):
#     # Get movie name and use it to pass it as an argument to the youtube api.
#     movie_name = movies['original_title']
#     youtube = build( YOUTUBE)
#     search_response = youtube.search().list(q=movie_name, part='id,snippet', maxResults=1).execute()
#     for search_result in search_response.get('items', []):
#         if search_result['id']['kind'] == 'youtube#video':
#             video_id = search_result['id']['videoId']
#         return render(request, 'youtube_movie.html', {'movies':movies, 'videoId':video_id})

def indexpage(request,category):
    key =  config('API_KEY')  
    url =  config('url') 
    url2 = url.format(category,key)
    urll = requests.get(url2)
    urlll = urll.json()
    return urlll

def youtube(request,id):
    YOUTUBE =  config('YOUTUBE_API_KEY') 
    popular = indexpage(request,'popular')
    pp = ''
    for p in popular['results']:
        if str(p['id'])==str(id):
            pp = p['title']
    youtube = build('youtube','v3',developerKey = YOUTUBE)
    req = youtube.search().list(q= pp+'trailer',part = 'snippet',type= 'video')
    res = req.execute()
    return render(request,'youtube_movie.html',{'response':res})
