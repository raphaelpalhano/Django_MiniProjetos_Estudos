from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("Mensage", views.Mensage, name="Mensage"),
    path("<str:name>", views.Named, name="Named")
]