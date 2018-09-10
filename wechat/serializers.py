# coding: utf-8
# @Author: ericlfay
# @Date:   2018-09-10 13:39:07

from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
