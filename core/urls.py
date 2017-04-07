from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^logout/$', views.logout_user, name="logout"),
    url(r'^new/$', views.new_user, name="newuser"),

]
