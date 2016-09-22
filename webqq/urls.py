#!/usr/bin/env python
# Name: urls.py
# Time:8/4/16 3:01 PM
# Author:luo1fly

from django.conf.urls import include, url
from webqq import views

urlpatterns = [
    url(r'^$', views.dashboard, name='chatroom'),
    url(r'^send_msg/$', views.send_msg, name='chat_send_msg'),
    url(r'^get_msg/$', views.get_msg, name='get_new_msg'),
]
