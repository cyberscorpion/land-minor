from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url
from .views import *
urlpatterns = [
    path('login', login_page, name="login"),
    path('check', auth_check, name="check"),
#    path('invalid', invalid, name="invalid"),
    path('logout', logout_user, name="logout"),
    path('register', register_user, name="register"),

]
