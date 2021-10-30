from django.db import models
from django.db.models import CASCADE
from entities.models import Movie, Book, Theater, Song, Journey
from django.contrib.auth.models import User


# Create your models here.

class MoviePerception(models.Model):
    # profile = models.ForeignKey('Profile')
    entity = models.ForeignKey('entities.Movie', on_delete=CASCADE, verbose_name='فیلم')
    perception = models.TextField('ادراک')
