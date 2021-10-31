from django.db import models
from django.db.models import CASCADE
from entities.models import Movie, Book, Theater, Song, Journey
from accounts.models import Profile


# Create your models here.

class CommonFields(models.Model):
    class Meta:
        abstract = True

    profile = models.ForeignKey('accounts.Profile', on_delete=CASCADE, verbose_name='نمایه کاربر')
    perception = models.TextField('ادراک')


class MoviePerception(CommonFields):
    entity = models.ForeignKey('entities.Movie', on_delete=CASCADE, verbose_name='فیلم')


class BookPerception(CommonFields):
    entity = models.ForeignKey('entities.Book', on_delete=CASCADE, verbose_name='کتاب')


class TheaterPerception(CommonFields):
    entity = models.ForeignKey('entities.Theater', on_delete=CASCADE, verbose_name='تئاتر')


class SongPerception(CommonFields):
    entity = models.ForeignKey('entities.Song', on_delete=CASCADE, verbose_name='ترانه')


class JourneyPerception(CommonFields):
    entity = models.ForeignKey('entities.Journey', on_delete=CASCADE, verbose_name='سفر')