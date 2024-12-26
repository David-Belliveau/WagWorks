from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("records/register.html/", views.register, name="register"),
    path("records/about.html/", views.about, name="about"),

]
