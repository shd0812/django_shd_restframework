#! /usr/bin/env python

# -*- coding: utf-8 -*-

# @Time 2020/11/15 22:41
# @Author  cunfu
# @File projectserializers.py
from apps.projects.models import Projects
from apps.debugtalks.models import DebugTalks
from rest_framework import serializers


class ProjectSerializers(serializers.ModelSerializer):

    class Meta:
        model = Projects
        exclude = ('update_time', 'is_delete')

        extra_kwargs = {
            'create_time': {
                'read_only': True
            }
        }

    def create(self, validated_data):
        project = super().create(validated_data)
        DebugTalks.objects.create(project=project)

        return project
