from django.urls import path

from .views import index, about, shipping

app_name = "main"

urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("shipping/", shipping, name="shipping"),
]
