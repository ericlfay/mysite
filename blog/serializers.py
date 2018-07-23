# -*- coding: utf-8 -*-
# @Author: ericlfay
# @Date:   2018-07-23 15:17:20
from rest_framework import serializers

from .models import Blog

class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = "__all__"
