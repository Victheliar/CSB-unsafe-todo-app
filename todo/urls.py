from django.urls import path
from . import views

urlpatterns = [
    path("", views.homePageView, name="index"),
    path("register/", views.registerPageView),
]