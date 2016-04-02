from django.conf.urls import url
from webuser import views

urlpatterns = [
    url(r'^', views.home),
]
