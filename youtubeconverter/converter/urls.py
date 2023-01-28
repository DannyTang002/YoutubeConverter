from django.urls import path
from .import views

app_name = "converter"

urlpatterns = [
    path("register/", views.register_view, name="register"),
]