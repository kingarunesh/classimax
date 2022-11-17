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
from django.views.generic.edit import FormMixin
from friends.models import Follow


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



# class ContactAdUserView(LoginRequiredMixin, CreateView):
#     model = ContactUser
#     template_name = "publicprofile/contact.html"
#     form_class = CreateContactForm

#     def get_context_data(self, **kwargs):
#         context = super(ContactAdUserView, self).get_context_data(**kwargs)
#         context["profile"] = self.request.user
#         return context

class ContactAdUserView(LoginRequiredMixin, DetailView, FormMixin):
    model = User
    template_name = "publicprofile/contact.html"
    form_class = CreateContactForm

    def get_context_data(self, **kwargs):
        context = super(ContactAdUserView, self).get_context_data(**kwargs)
        # context["profile"] = self.request.user
        context["profile"] = User.objects.get(pk=self.kwargs["pk"])
        return context
    
    def form_valid(self, form, **kwargs):
        form.instance.sender_user = self.request.user
        form.instance.receiver_user = User.objects.get(pk=self.kwargs["pk"])
        form.save()
        return super(ContactAdUserView, self).form_valid(form)
    
    def post(self, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy("publicprofile:public_profile", kwargs={"pk": self.kwargs["pk"]})
    
    def get(self, request, *args, **kwargs):
        ad_user = User.objects.get(id=kwargs["pk"])

        if ad_user == request.user:
            return HttpResponseRedirect("/")
        
        return super(ContactAdUserView, self).get(request, *args, **kwargs)


class UsersListView(LoginRequiredMixin, ListView):
    template_name = "publicprofile/user-list.html"
    model = Account
    context_object_name = "users"

    def get_queryset(self):
        return Account.objects.all().order_by("-id")


class FollowingsDetailView(LoginRequiredMixin, DetailView):
    model = Follow
    template_name = "publicprofile/following.html"
    context_object_name = "xyz"
    
    def get_context_data(self, **kwargs):
        context = super(FollowingsDetailView, self).get_context_data(**kwargs)
        context["profile"] = Account.objects.get(id=self.kwargs["pk"])
        context["followings"] = Follow.objects.filter(following=self.kwargs["pk"]).order_by("-date")
        return context


class FollowersDetailView(LoginRequiredMixin, DetailView):
    model = Follow
    template_name = "publicprofile/followers.html"
    context_object_name = "abc"
    
    def get_context_data(self, **kwargs):
        context = super(FollowersDetailView, self).get_context_data(**kwargs)
        context["profile"] = Account.objects.get(id=self.kwargs["pk"])
        context["followers"] = Follow.objects.filter(followers=self.kwargs["pk"]).order_by("-date")
        return context