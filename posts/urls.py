from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.index, name="home"),
    path("about", views.about, name="about"),
    path("post", views.post, name="post"),
    path("contact", views.contact, name="contact"),
]
