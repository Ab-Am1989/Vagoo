from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import DetailView, CreateView
from .models import Profile
from .form import ProfileCreateForm, UserForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages


# Create your views here.

class Login(LoginView):
    template_name = 'accounts/loginview_form.html'


class CreateProfile(LoginRequiredMixin, CreateView):
    model = Profile
    template_name = 'accounts/profile_create.html'
    login_url = 'accounts:login'
    fields = ['mobile', 'gender', 'birth_date', 'country', 'city', 'profile_image']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super().form_valid(form)


class ProfileDetails(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'accounts/profile_details.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return self.request.user.profile
