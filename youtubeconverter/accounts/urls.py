from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views 


app_name = "accounts"


urlpatterns = [
    path("signup/",views.signup_view,name="signup"),
    path("login/",views.login_view,name="login"),
    path("logout/", views.logout_view , name="logout")
]

