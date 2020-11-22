#! /usr/bin/env python

# -*- coding: utf-8 -*-

# @Time 2020/11/18 07:18
# @Author  cunfu
# @File urls.py


from django.urls import path, re_path
from apps.projects import views


urlpatterns = [
    path('name/', views.ProjectsView.as_view({'get': 'names'})),

    path('', views.ProjectsView.as_view({'get':'list', 'post':'create'})),
    path('<int:pk>/interfaces/', views.ProjectsView.as_view(
        {'get': 'retrieve', "delete": "destroy", 'put': "update", "patch": "partial_update", })),

]