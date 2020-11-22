#! /usr/bin/env python

# -*- coding: utf-8 -*-

# @Time 2020/11/14 23:05
# @Author  cunfu
# @File urls.py


from django.urls import path, re_path
from apps.users import views
from  rest_framework_jwt.views import obtain_jwt_token




urlpatterns = [


    # path('login/', obtain_jwt_token),
    path('register/', views.RegisterView.as_view()),
    path('users/', views.UserInfoView.as_view(
        {
            'get': 'list',
            'post': 'create'
        }
    )),
    # re_path(r'^(?P<username>\w{6,20}/count/$)', views.UserValidView.as_view()),
    re_path(r'^(?P<username>\w{1,10}/count/$)', views.UserValidView.as_view()),
    path('users/', views.UserInfoView.as_view(
        {'get': 'retrieve',
         "delete": "destroy",
         'put': "update", "patch":
         "partial_update"
         }
    )),
    path('users/<int:pk>/desc/', views.UserInfoView.as_view(
        {
            'get': 'display',
            'post': 'add'
        }
    )),

]