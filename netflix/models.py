from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class UserProfile(models.Model):
  username = models.CharField(max_length=100)
  tagline = models.CharField(max_length=250)
  photo_path = models.ImageField(upload_to = 'profiles/')
  user = models.ForeignKey(User, on_delete=CASCADE )

