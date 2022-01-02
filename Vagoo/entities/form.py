from .models import Movie, Book, Theater, Song, Journey, JourneyImages
from django import forms
from django.contrib.gis import forms
from location_field.forms.plain import PlainLocationField
from django.db.models import Q
from django.core.exceptions import ValidationError


class MovieCreateForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

    def clean(self):
        super().clean()
        name = self.cleaned_data.get('name')
        director = self.cleaned_data.get('director')
        year = self.cleaned_data.get('year')

        if Movie.objects.filter(Q(name__contains=name) & Q(director__contains=
                                                           director) & Q(year=year)):
            raise ValidationError('This movie has been added to our library yet!')


class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author', 'publisher', 'isbn', 'subject', 'image']

    def clean_isbn(self):
        isbn = self.cleaned_data['isbn']

        if Book.objects.filter(isbn=isbn):
            raise ValidationError('This book has been added to our library yet!')
        return isbn


class TheaterCreateForm(forms.ModelForm):
    class Meta:
        model = Theater
        fields = '__all__'

    def clean(self):
        super().clean()
        name = self.cleaned_data.get('name')
        director = self.cleaned_data.get('director')
        scriptwriter = self.cleaned_data.get('scriptwriter')

        if Theater.objects.filter(Q(name__contains=name) & Q(director__contains=director)):
            if Theater.objects.filter(scriptwriter__contains=scriptwriter):
                raise ValidationError('This theater has been added to our library yet!')


class SongCreateForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = '__all__'

    def clean(self):
        super().clean()
        name = self.cleaned_data.get('name')
        singer = self.cleaned_data.get('singer')
        songwriter = self.cleaned_data.get('songwriter')
        composer = self.cleaned_data.get('composer')
        if Song.objects.filter(Q(name__contains=name) & Q(singer__contains=singer) & Q(composer__contains=composer) & Q(
                songwriter__contains=songwriter)):
            raise ValidationError('This song has been added to our library yet!')


class JourneyCreateForm(forms.ModelForm):
    # location = forms.PointField()

    class Meta:
        model = Journey
        fields = ('title', 'city', 'location', 'country', 'province')

