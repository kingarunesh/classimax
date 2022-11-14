from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    username = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200)
    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta(UserCreationForm):
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")