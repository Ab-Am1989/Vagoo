from django.urls import path
from .views import Login, ProfileDetails, CreateProfile
from django.contrib.auth.views import LogoutView

app_name = 'accounts'

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/details/', ProfileDetails.as_view(), name='profile_details'),
    path('profile/edit/', CreateProfile.as_view(), name='profile_create'),
]
