from django.urls import path, include
from . import views

app_name = "urlsaver"

urlpatterns = [
    path("", views.indexView, name="index"),
    path("api/", include("urlsaver.api.urls")),
]
