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
from friends.models import Follow
from django.contrib.auth import get_user_model
User = get_user_model()



class UserProfileView(LoginRequiredMixin, ListView):
    model = PostAD
    template_name = "dashboard/profile.html"
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(*kwargs)
        context["profile"] = self.request.user
        context["total_followers"] = Follow.objects.filter(following=self.request.user).count()
        context["total_followings"] = Follow.objects.filter(user=self.request.user).count()
        context["total_ads"] = PostAD.objects.filter(user=self.request.user).count()
        context["total_bookmarks"] = Bookmark.objects.filter(user=self.request.user).count()
        context["total_contacts"] = ContactUser.objects.filter(receiver_user=self.request.user).count()
        return context
    
    def get_queryset(self):
        return PostAD.objects.filter(user=self.request.user).order_by("-id")


class UpdateUserProfile(LoginRequiredMixin, UpdateView):
    model = Account
    template_name = "dashboard/update-user-profile.html"
    form_class = UserProfileUpdateForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(UpdateUserProfile, self).form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy("dashboard:profile")

    def get_context_data(self, **kwargs):
        context = super(UpdateUserProfile, self).get_context_data(*kwargs)
        context["profile"] = self.request.user
        context["total_followers"] = Follow.objects.filter(following=self.request.user).count()
        context["total_followings"] = Follow.objects.filter(user=self.request.user).count()
        context["total_ads"] = PostAD.objects.filter(user=self.request.user).count()
        context["total_bookmarks"] = Bookmark.objects.filter(user=self.request.user).count()
        context["total_contacts"] = ContactUser.objects.filter(receiver_user=self.request.user).count()
        return context
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object != request.user:
            return HttpResponseRedirect("/")
        
        return super(UpdateUserProfile, self).get(request, *args, **kwargs)


class MyAdPostView(LoginRequiredMixin, ListView):
    model = PostAD
    template_name = "dashboard/my-ad-post.html"
    context_object_name = "adposts"
    paginate_by = 9

    def get_queryset(self):
        return PostAD.objects.filter(user=self.request.user).order_by("-id")
    
    def get_context_data(self, **kwargs):
        context = super(MyAdPostView, self).get_context_data(**kwargs)
        context["profile"] = self.request.user
        context["total_followers"] = Follow.objects.filter(following=self.request.user).count()
        context["total_followings"] = Follow.objects.filter(user=self.request.user).count()
        context["total_ads"] = PostAD.objects.filter(user=self.request.user).count()
        context["total_bookmarks"] = Bookmark.objects.filter(user=self.request.user).count()
        context["total_contacts"] = ContactUser.objects.filter(receiver_user=self.request.user).count()
        return context


class BookmarkAdPostView(LoginRequiredMixin, ListView):
    model = Bookmark
    template_name = "dashboard/bookmark-ad-posts.html"
    context_object_name = "bookmarks"
    paginate_by = 9

    def get_queryset(self):
        return Bookmark.objects.filter(user=self.request.user).order_by("-id")

    def get_context_data(self, **kwargs):
        context = super(BookmarkAdPostView, self).get_context_data(**kwargs)
        context["profile"] = self.request.user
        context["total_followers"] = Follow.objects.filter(following=self.request.user).count()
        context["total_followings"] = Follow.objects.filter(user=self.request.user).count()
        context["total_ads"] = PostAD.objects.filter(user=self.request.user).count()
        context["total_bookmarks"] = Bookmark.objects.filter(user=self.request.user).count()
        context["total_contacts"] = ContactUser.objects.filter(receiver_user=self.request.user).count()
        return context


class ContactUserView(LoginRequiredMixin, ListView):
    model = ContactUser
    template_name = "dashboard/contacts.html"
    context_object_name = "contacts"
    paginate_by = 9

    def get_queryset(self):
        return ContactUser.objects.filter(receiver_user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(ContactUserView, self).get_context_data(**kwargs)
        context["profile"] = self.request.user
        context["total_followers"] = Follow.objects.filter(following=self.request.user).count()
        context["total_followings"] = Follow.objects.filter(user=self.request.user).count()
        context["total_ads"] = PostAD.objects.filter(user=self.request.user).count()
        context["total_bookmarks"] = Bookmark.objects.filter(user=self.request.user).count()
        context["total_contacts"] = ContactUser.objects.filter(receiver_user=self.request.user).count()
        return context


class SendContactView(LoginRequiredMixin, CreateView):
    model = ContactUser
    template_name = "dashboard/send-contact.html"
    form_class = CreateContactForm

    def get_context_data(self, **kwargs):
        context = super(SendContactView, self).get_context_data(**kwargs)
        context["profile"] = self.request.user
        return context


class FollowingsListView(LoginRequiredMixin, ListView):
    model = Follow
    template_name = "dashboard/following.html"
    context_object_name = "followings"

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user).order_by("-date")
    
    def get_context_data(self, **kwargs):
        context = super(FollowingsListView, self).get_context_data(**kwargs)
        context["profile"] = self.request.user
        context["total_followers"] = Follow.objects.filter(following=self.request.user).count()
        context["total_followings"] = Follow.objects.filter(user=self.request.user).count()
        context["total_ads"] = PostAD.objects.filter(user=self.request.user).count()
        context["total_bookmarks"] = Bookmark.objects.filter(user=self.request.user).count()
        context["total_contacts"] = ContactUser.objects.filter(receiver_user=self.request.user).count()
        return context


class FollowersListView(LoginRequiredMixin, ListView):
    model = Follow
    template_name = "dashboard/followers.html"
    context_object_name = "followers"

    def get_queryset(self):
        return Follow.objects.filter(following=self.request.user).order_by("-date")
    
    def get_context_data(self, **kwargs):
        context = super(FollowersListView, self).get_context_data(**kwargs)
        context["profile"] = self.request.user
        context["total_followers"] = Follow.objects.filter(following=self.request.user).count()
        context["total_followings"] = Follow.objects.filter(user=self.request.user).count()
        context["total_ads"] = PostAD.objects.filter(user=self.request.user).count()
        context["total_bookmarks"] = Bookmark.objects.filter(user=self.request.user).count()
        context["total_contacts"] = ContactUser.objects.filter(receiver_user=self.request.user).count()
        return context