# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.allblogs, name = 'allblogs'),
    url(r'(?P<blog_id>\d+)/', views.detail, name='detail'),
    # path('<int:blog_id>/', views.detail, name='detail')
]