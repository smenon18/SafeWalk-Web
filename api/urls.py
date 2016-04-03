from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^check_login/', views.check_login),
    url(r'^notify_parent/', views.notify_parent),
    url(r'^create_user/', views.create_user),
    url(r'^list_users/', views.list_users),
]

