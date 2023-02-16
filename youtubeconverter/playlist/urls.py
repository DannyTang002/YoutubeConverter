from django.urls import path
from .import views

app_name = "playlist"

urlpatterns = [
    path("register/", views.register_playlist, name="register"),
    path("listed/", views.listed_playlist, name="listed"),
    path("info/<slug>", views.show_info, name="info"),
]