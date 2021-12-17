from django.shortcuts import render
from django.views.generic import DetailView, CreateView, ListView
from .models import Movie, Book, Theater, Song, Journey
from .form import MovieCreateForm, BookCreateForm, TheaterCreateForm, SongCreateForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse


# Create your views here.

class MovieCreate(CreateView):
    model = Movie
    template_name = 'entities/movie_create.html'
    form_class = MovieCreateForm


class MovieShowList(ListView):
    model = Movie
    template_name = 'entities/movie_list.html'
    context_object_name = 'movies'


class MovieShowDetails(DetailView):
    model = Movie
    template_name = 'entities/movie_details.html'
    context_object_name = 'movie_details'


class BookCreate(CreateView):
    model = Book
    template_name = 'entities/book_create.html'
    form_class = BookCreateForm


class BookShowList(ListView):
    model = Book
    template_name = 'entities/book_list.html'
    context_object_name = 'books'


class BookShowDetails(DetailView):
    model = Book
    template_name = 'entities/book_details.html'
    context_object_name = 'book_details'


class TheaterCreate(CreateView):
    model = Theater
    template_name = 'entities/theater_create.html'
    form_class = TheaterCreateForm


class TheaterShowList(ListView):
    model = Theater
    template_name = 'entities/theater_list.html'
    context_object_name = 'theaters'


class TheaterShowDetails(DetailView):
    model = Theater
    template_name = 'entities/theater_details.html'
    context_object_name = 'theater_details'


class SongCreate(CreateView):
    model = Song
    template_name = 'entities/song_create.html'
    form_class = SongCreateForm


class SongShowList(ListView):
    model = Song
    template_name = 'entities/song_list'
    context_object_name = 'songs'


class SongShowDetails(DetailView):
    model = Song
    template_name = 'entities/song_details.html'
    context_object_name = 'song_details'
