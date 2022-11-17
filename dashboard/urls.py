from django.urls import path
from dashboard.views import *
from friends.views import *


app_name = "dashboard"

urlpatterns = [
    path("profile/", UserProfileView.as_view(), name="profile"),
    path("update-profile/<int:pk>/", UpdateUserProfile.as_view(), name="update_profile"),
    path("my-ad-posts/", MyAdPostView.as_view(), name="my_adposts"),
    path("bookmarks/", BookmarkAdPostView.as_view(), name="bookmark_adposts"),
    path("contacts/", ContactUserView.as_view(), name="user_contacts"),
    path("send-contact/", SendContactView.as_view(), name="send_contact"),
    path("following/", FollowingsListView.as_view(), name="following"),
    path("followers/", FollowersListView.as_view(), name="followers")

]