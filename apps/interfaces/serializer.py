#! /usr/bin/env python

# -*- coding: utf-8 -*-

# @Time 2020/11/20 21:44
# @Author  cunfu
# @File serializer.py

from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Interfaces
from apps.projects.models import Projects

class InterfaceSerializer(ModelSerializer):

    project = serializers.StringRelatedField(help_text="项目名称")
    project_id = serializers.PrimaryKeyRelatedField(queryset=Projects.objects.all())
    siwa = serializers.CharField(source='project.name', read_only=True)
    class Meta:
        model = Interfaces
        fields = ('id', 'name', 'tester', 'desc', 'create_time', 'project', 'siwa', 'project_id')

        extra_kwargs = {
            'create_time': {
                'read_only': True
            }
        }

    def create(self, validated_data):
        project = validated_data.pop("project_id")
        validated_data['project'] = project
        interface = Interfaces.objects.create(**validated_data)
        return interface
