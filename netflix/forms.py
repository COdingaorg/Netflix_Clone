from netflix.models import Playlist, UserProfile
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class registerUserForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class add_profile_form(forms.ModelForm):
  class Meta:
    model = UserProfile
    fields = ('photo_path', 'username', 'tagline')

class addplaylist_form(forms.ModelForm):
  class Meta:
    model = Playlist
    fields = ('movie_id','original_language','original_title','overview','popularity','poster_path','release_date','vote_average','vote_count')
