from django.shortcuts import render
from django.views.generic import DetailView, CreateView, ListView
from .models import Movie, Book, Theater, Song, Journey
from .form import MovieCreateForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse


# Create your views here.

class MovieCreate(CreateView):
    model = Movie
    template_name = 'entities/movie_create.html'
    form_class = MovieCreateForm
    context_object_name = 'create_form'


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
    fields = ['name', 'author', 'publisher', 'subject', 'image']


class TheaterCreate(CreateView):
    model = Theater
    fields = ['name', 'director', 'genre', 'image']
