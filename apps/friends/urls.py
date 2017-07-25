from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^/findfriend', views.findfriend),
    url(r'^/addfriend/(?P<id>\d+)$', views.addfriend),
    url(r'^/viewfriends', views.viewfriends),
    url(r'^/delete/(?P<id>\d+)$', views.remove)
]
