from django.urls import path
from .views import MovieCreate, MovieShowDetails, MovieShowList, BookCreate, BookShowList, BookShowDetails

app_name = 'entities'

urlpatterns = [
    path('movies/create/', MovieCreate.as_view(), name='movies_create'),
    path('movies/<int:pk>/', MovieShowDetails.as_view(), name='movies_details'),
    path('movies/list/', MovieShowList.as_view(), name='movies_list'),
    path('books/create/', BookCreate.as_view(), name='books_create'),
    path('books/list/', BookShowList.as_view(), name='books_list'),
    path('books/<int:pk>/', BookShowDetails.as_view(), name='books_details'),

]
