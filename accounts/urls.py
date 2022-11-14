from django.urls import path
from accounts.views import *


app_name = "accounts"

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register")
]