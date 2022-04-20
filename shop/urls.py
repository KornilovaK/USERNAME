from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("reservation", views.reservation, name="reservation"),
    path("reservation/make", views.make, name="make"),
    path("menu", views.menu, name="menu")
]