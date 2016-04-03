from django.conf.urls import url
from webuser import views

urlpatterns = [
    url(r'^login', views.login, name="webuser-views-login"),
    url(r'^register', views.register, name="webuser-views-register"),
    url(r'^confirm', views.confirm, name="webuser-views-confirm"),
    url(r'^', views.home, name="webuser-views-home"),
]
