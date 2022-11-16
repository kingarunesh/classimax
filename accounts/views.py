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



class RegisterView(CreateView):
    template_name = "accounts/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("accounts:login")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect("/")
        return super(RegisterView, self).dispatch(request, *args, **kwargs)


class LoginUserView(LoginView):
    template_name = "accounts/login.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect("/")
        return super(LoginUserView, self).dispatch(request, *args, **kwargs)


class LogoutUserView(LogoutView):
    template_name = "accounts/register.html"

