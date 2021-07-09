from django.conf.urls import url
from netflix import views

urlpatterns = [
  url(r'^$', views.login_user, name = 'login'),
  url(r'^logout/$', views.logout_user, name = 'logout'),
  url(r'^movie_slack/$', views.index, name = 'home'),
  url(r'^search_results/$', views.search_movies, name = 'search_movies'),
  ]