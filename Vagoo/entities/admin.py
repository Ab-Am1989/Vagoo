from django.contrib import admin

from entities.models import Journey, Movie, Book, Theater, Song, JourneyImages

admin.site.register(Journey)
admin.site.register(Movie)
admin.site.register(Book)
admin.site.register(Theater)
admin.site.register(Song)
admin.site.register(JourneyImages)

