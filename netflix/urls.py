from django.conf.urls import url
from netflix import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
  url(r'^$', views.register_user, name = 'register'),
  url(r'^login/', views.login_user, name = 'login'),
  url(r'^logout/$', views.logout_user, name = 'logout'),
  url(r'^home/$', views.index, name = 'home'),
  url(r'^search_results/$', views.search_movies, name = 'search_movies'),
  url(r'user_profile/$', views.add_user_profile, name = 'profile'),
  url(r'^movie/(\d+)', views.youtube, name = 'netflix'),
  ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)