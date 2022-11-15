from django.urls import path
from accounts.views import *


app_name = "accounts"

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginUserView.as_view(), name="login"),
    path("logout/", LogoutUserView.as_view(), name="logout"),
    path("profile/", UserProfileView.as_view(), name="profile"),
    path("update-profile/<int:pk>/", UpdateUserProfile.as_view(), name="update_profile"),
    path("my-ad-posts/", MyAdPostView.as_view(), name="my_adposts"),
]