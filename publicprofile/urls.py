from django.urls import path
from publicprofile.views import *

app_name = "publicprofile"

urlpatterns = [
    path("profile/<int:pk>/", PublicUserProfileView.as_view(), name="public_profile"),
]