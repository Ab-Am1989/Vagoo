from django.urls import path
from .views import MovieCreate, MovieShowDetails, MovieShowList

app_name = 'entities'

urlpatterns = [
    path('movies/create/', MovieCreate.as_view(), name='movies_create'),
    path('movies/<int:pk>/', MovieShowDetails.as_view(), name='movies_details'),
    path('movies/list/', MovieShowList.as_view(), name='movies_list')
]
