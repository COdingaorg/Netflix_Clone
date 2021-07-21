from netflix.models import UserProfile
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
    fields = ('__all__')
