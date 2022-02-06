from .models import Profile
from django import forms
from django.contrib.auth.forms import UserChangeForm


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'mobile', 'gender', 'birth_date', 'country', 'city', 'profile_image']


class UserForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        fields = ['first_name', 'last_name', 'email']
