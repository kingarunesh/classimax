from django.urls import path
from postad.views import *


app_name = "postad"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("posts/", PostAdView.as_view(), name="posts"),
    path("post/<int:pk>/<slug:slug>/", PostAdDetailView.as_view(), name="postad_detail"),
    path("create-postad/", PostAdCreateView.as_view(), name="create_postad")
]