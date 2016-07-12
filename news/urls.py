# coding:utf-8
# __author__ = 'BianXuesheng'
# __data__ = '2016/07/12_12:02 '

from django.conf.urls import patterns, url
from news import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
