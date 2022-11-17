from django.urls import path
from postad.views import *


app_name = "postad"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("adposts/", PostAdView.as_view(), name="adposts"),
    path("post/<int:pk>/<slug:slug>/", PostAdDetailView.as_view(), name="postad_detail"),
    path("create-postad/", PostAdCreateView.as_view(), name="create_postad"),
    path("update/<int:pk>/<slug:slug>/", UpdatePostAdView.as_view(), name="update_postad"),
    path("delete/<int:pk>/<slug:slug>", DeletePostAdView.as_view(), name="delete_adpost"),
    path("search-result/", SearchResultView.as_view(), name="search_results")
]