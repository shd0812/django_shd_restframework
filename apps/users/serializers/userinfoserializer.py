#! /usr/bin/env python

# -*- coding: utf-8 -*-

# @Time 2020/11/14 23:08
# @Author  cunfu
# @File userinfoserializer.py
from rest_framework import serializers
from apps.users import models


class UserInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.UserInfo
        fields = '__all__'