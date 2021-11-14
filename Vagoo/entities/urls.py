from django.urls import path
from .views import MovieCreate, MovieShowDetails

app_name = 'entities'

urlpatterns = [
    path('create/new_movie/', MovieCreate.as_view(), name='create_newMovie'),
    path('movies/<int:pk>', MovieShowDetails.as_view(), name='movie_details'),
]
