#! /usr/bin/env python

# -*- coding: utf-8 -*-

# @Time 2020/11/18 07:22
# @Author  cunfu
# @File serializer.py


from apps.projects.models import Projects
from rest_framework import serializers



class ProjectsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Projects
        exclude = ('update_time', 'is_delete')

        extra_kwargs = {
            'create_time': {
                'read_only': True
            }
        }


class ProjectSerializerNameandId(serializers.ModelSerializer):

    class Meta:
        model = Projects
        fields = ('id', 'name')
