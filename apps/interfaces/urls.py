#! /usr/bin/env python

# -*- coding: utf-8 -*-

# @Time 2020/11/20 21:40
# @Author  cunfu
# @File urls.py


from django.urls import path, re_path
from apps.interfaces import views


urlpatterns = [
    path('', views.InterfaceView.as_view({'get':'list', 'post':'create'})),
    path('<int:pk>/interfaces/', views.InterfaceView.as_view(
        {'get': 'retrieve', "delete": "destroy", 'put': "update", "patch": "partial_update", })),

]