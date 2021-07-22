from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import IntegerField

# Create your models here.
class UserProfile(models.Model):
  username = models.CharField(max_length=100)
  tagline = models.CharField(max_length=250)
  photo_path = models.ImageField(upload_to = 'profiles/')
  user = models.ForeignKey(User, on_delete=CASCADE )

  class Meta:
    ordering = ['-id']

class Playlist(models.Model):
  movie_id=models.IntegerField()
  original_language = models.CharField(max_length=100)
  original_title = models.CharField(max_length=200)
  overview = models.TextField()
  popularity = models.FloatField()
  poster_path = models.CharField(max_length=200)
  release_date = models.CharField(max_length=200)
  vote_average = models.FloatField()
  vote_count = models.IntegerField(default=0)

  date_added = models.DateTimeField()
  user_profile = models.ForeignKey(UserProfile, on_delete=CASCADE)