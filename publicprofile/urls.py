from django.urls import path
from publicprofile.views import *

app_name = "publicprofile"

urlpatterns = [
    path("profile/<int:pk>/", PublicUserProfileView.as_view(), name="public_profile"),
    path("ad-posts/<int:pk>/", AdPostPublicView.as_view(), name="ad_posts"),
    path("contact/<int:pk>/", ContactAdUserView.as_view(), name="contact_ad_user"),
    path("following/<int:pk>/", FollowingsDetailView.as_view(), name="following"),
    path("followers/<int:pk>/", FollowersDetailView.as_view(), name="followers"),
    path("users/", UsersListView.as_view(), name="user_list")
]