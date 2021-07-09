from django.conf.urls import url
from netflix import views

urlpatterns = [
  url(r'^$', views.index, name = 'home'),
  url(r'search_results/$', views.search_movies, name = 'search_movies'),
  ]