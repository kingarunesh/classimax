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


class AdPostPublicView(LoginRequiredMixin, ListView):
    model = PostAD
    template_name = "publicprofile/ad-post-list.html"
    context_object_name = "posts"

    def get_queryset(self):
        return PostAD.objects.filter(user=self.request.user).order_by("-id")
    
    def get_context_data(self, **kwargs):
        context = super(AdPostPublicView, self).get_context_data(**kwargs)
        user_data = User.objects.get(id=self.kwargs["pk"])
        context["adposts"] = PostAD.objects.filter(user=user_data).order_by("-id")
        context["total_adpost"] = PostAD.objects.filter(user=user_data).count()
        context["profile"] = user_data
        return context
