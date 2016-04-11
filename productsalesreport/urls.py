from django.conf.urls import url
from . import views
__author__ = 'Charles'

urlpatterns = [
    url(r'^$', views.index, name='index.html'),
]