from django.urls import path
from postad.views import *


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("posts/", PostAdView.as_view(), name="posts"),
]