from django.urls import path, include
from . import views

appname = "urlsaver"

urlpatterns = [
    path("", views.indexView, name="index"),
    path("api/", include("urlsaver.api.urls")),
]
