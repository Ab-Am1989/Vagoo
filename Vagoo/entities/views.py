from django.shortcuts import render
from django.views.generic import DetailView, CreateView
from .models import Movie, Book, Theater, Song, Journey
from .form import MovieCreateForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse


# Create your views here.

class MovieCreate(CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': MovieCreateForm()}
        return render(request, 'entities/movie-create.html', context)

    def post(self, request, *args, **kwargs):
        form = MovieCreateForm(request.POST)
        if form.is_valid():
            movie = form.save()
            movie.save()
            return HttpResponseRedirect(reverse_lazy('entities:movie_details', args=[movie.id]))
        return render(request, 'entities/movie-create.html', {'form': form})


class MovieShowDetails(DetailView):
    template_name = 'entities/movie_deatails.html'
    model = Movie


class BookCreate(CreateView):
    model = Book
    fields = ['name', 'author', 'publisher', 'subject', 'image']


class TheaterCreate(CreateView):
    model = Theater
    fields = ['name', 'director', 'genre', 'image']
