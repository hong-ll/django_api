# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     serializers
   Description :
   Author :       7326
   date：          2017/12/6
-------------------------------------------------
   Change Activity: 2017/12/6
-------------------------------------------------
"""
__author__ = '7326'


from rest_framework import serializers
from .models import User,Link

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=20)

class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20)
    name = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=20)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','name')


class LinkBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ('name','url')


class CrateLinkSerializer(LinkBaseSerializer):
    pass

class EditLinkSerializer(LinkBaseSerializer):
    id = serializers.IntegerField()