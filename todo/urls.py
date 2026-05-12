from django.urls import path
from . import views

urlpatterns = [
    path("", views.homePageView, name="index"),
    path("register/", views.registerPageView),
    path("login/", views.loginPageView),
    path("add_todo/", views.homePageView),
    path("delete_todo/", views.homePageView),
]