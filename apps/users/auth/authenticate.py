#! /usr/bin/env python

# -*- coding: utf-8 -*-

# @Time 2020/11/14 23:39
# @Author  cunfu
# @File authenticate.py


from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import  AuthenticationFailed

class AuthTicate(BaseAuthentication):

    def authenticate(self, request):
        print(request.headers)
        token = request.headers.get('token')
        if not token:
            raise AuthenticationFailed("认证失败")
        return (token, token)

    def authenticate_header(self, request):
        pass