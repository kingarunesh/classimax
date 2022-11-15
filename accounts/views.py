from django.views.generic import TemplateView, CreateView, DetailView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.forms import RegisterForm, UserProfileUpdateForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.conf import settings
from accounts.models import Account
from postad.models import PostAD
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


class UserProfileView(LoginRequiredMixin, ListView):
    model = PostAD
    template_name = "accounts/profile.html"
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(*kwargs)
        context["profile"] = self.request.user
        return context
    
    def get_queryset(self):
        return PostAD.objects.filter(user=self.request.user).order_by("-id")


class UpdateUserProfile(LoginRequiredMixin, UpdateView):
    model = Account
    template_name = "accounts/update-user-profile.html"
    form_class = UserProfileUpdateForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(UpdateUserProfile, self).form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy("accounts:profile")

    def get_context_data(self, **kwargs):
        context = super(UpdateUserProfile, self).get_context_data(*kwargs)
        context["profile"] = self.request.user
        return context
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object != request.user:
            return HttpResponseRedirect("/")
        
        return super(UpdateUserProfile, self).get(request, *args, **kwargs)