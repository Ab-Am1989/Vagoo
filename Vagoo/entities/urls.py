from django.urls import path
from .views import MovieCreate, MovieShowDetails, MovieShowList, BookCreate, BookShowList, BookShowDetails,\
    TheaterCreate, TheaterShowList, TheaterShowDetails, SongCreate, SongShowList, SongShowDetails


app_name = 'entities'

urlpatterns = [
    path('movies/create/', MovieCreate.as_view(), name='movies_create'),
    path('movies/<int:pk>/', MovieShowDetails.as_view(), name='movies_details'),
    path('movies/list/', MovieShowList.as_view(), name='movies_list'),
    path('books/create/', BookCreate.as_view(), name='books_create'),
    path('books/list/', BookShowList.as_view(), name='books_list'),
    path('books/<int:pk>/', BookShowDetails.as_view(), name='books_details'),
    path('theaters/create/', TheaterCreate.as_view(), name='theaters_create'),
    path('theaters/list/', TheaterShowList.as_view(), name='theaters_list'),
    path('theaters/<int:pk>/', TheaterShowDetails.as_view(), name='theaters_details'),
    path('songs/create/', SongCreate.as_view(), name='songs_create'),
    path('songs/list/', SongShowList.as_view(), name='songs_list'),
    path('songs/<int:pk>/', SongShowDetails.as_view(), name='songs_details'),
]
