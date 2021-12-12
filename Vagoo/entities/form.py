from .models import Movie, Book, Theater, Song, Journey, JourneyImages
from django import forms
from django.db.models import Q


class MovieCreateForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

    def clean(self):
        name = self.cleaned_data.get('name')
        director = self.cleaned_data.get('director')
        year = self.cleaned_data.get('year')

        if Movie.objects.filter(Q(name__contains=name) & Q(director=director) & Q(year=year)):
            return forms.ValidationError('This movie has been added to our library yet!')


class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn')

        if Book.objects.filter(isbn=isbn):
            return forms.ValidationError('This book has been added to our library yet!')
        return isbn


class TheaterCreateForm(forms.ModelForm):
    class Meta:
        model = Theater
        fields = '__all__'

    def clean(self):
        name = self.cleaned_data.get('name')
        director = self.cleaned_data.get('director')
        scriptwriter = self.cleaned_data.get('scriptwriter')

        if Theater.objects.filter(Q(name__contains=name) & Q(director=director) & Q(scriptwriter=scriptwriter)):
            return forms.ValidationError('This theater has been added to our library yet!')


class SongCreateForm(forms.ModelForm):
    class Meta:
        fields = '__all__'

    def clean(self):
        name = self.cleaned_data.get('name')
        singer = self.cleaned_data.get('singer')
        songwriter = self.cleaned_data.get('songwriter')
        composer = self.cleaned_data.get('composer')
        songs = Song.objects.filter(
            Q(name__contains=name) & Q(singer__contains=singer) & Q(composer__contains=composer) & Q(
                songwriter__contains=songwriter))
        if songs:
            return forms.ValidationError('This song has been added to our library yet!')


class JourneyCreateForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
