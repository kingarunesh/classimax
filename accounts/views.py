from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.forms import RegisterForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView, LogoutView



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


class SecretPageView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"