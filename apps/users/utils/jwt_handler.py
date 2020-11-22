#! /usr/bin/env python

# -*- coding: utf-8 -*-

# @Time 2020/11/15 15:07
# @Author  cunfu
# @File jwt_handler.py



def jwt_response_payload_handler(token, user=None, request=None):

    return {
        'token': token,
        'user_id': user.id,
        'user_name': user.username
    }
