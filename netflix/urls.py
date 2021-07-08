from django.conf.urls import url
from netflix import views

urlpatterns = [
  url(r'', views.index, name = 'home'),
  ]