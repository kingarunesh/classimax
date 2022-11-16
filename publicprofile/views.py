from django.views.generic import TemplateView, CreateView, DetailView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.forms import RegisterForm, UserProfileUpdateForm, CreateContactForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.conf import settings
from accounts.models import Account, ContactUser
from postad.models import PostAD, Bookmark

from django.contrib.auth import get_user_model
User = get_user_model()



class PublicUserProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "publicprofile/public-profile.html"
    context_object_name = "profile"