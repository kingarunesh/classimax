from django.urls import path
from postad.views import *


app_name = "postad"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("adposts/", PostAdView.as_view(), name="adposts"),
    path("post/<int:pk>/<slug:slug>/", PostAdDetailView.as_view(), name="postad_detail"),
    path("create-postad/", PostAdCreateView.as_view(), name="create_postad"),
    path("update/<int:pk>/<slug:slug>/", UpdatePostAdView.as_view(), name="update_postad")
]