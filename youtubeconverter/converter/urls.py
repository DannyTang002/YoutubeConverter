from django.urls import path
from .import views

app_name = "converter"

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("listed/", views.listed_view, name="listed"),
    path("convert/<slug>", views.video_convert, name="convert"),

]