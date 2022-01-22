from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView


# Create your views here.

class Login(LoginView):
    template_name = 'accounts/loginview_form.html'


class Logout(LogoutView):
    pass
