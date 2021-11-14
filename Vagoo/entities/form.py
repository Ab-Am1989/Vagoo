from entities.models import Movie, Book, Theater, Song, Journey, JourneyImages
from django import forms


class MovieCreateForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
