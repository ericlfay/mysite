# -*- coding: utf-8 -*-
# @Author: ericlfay
# @Date:   2018-07-23 15:17:20
from rest_framework import serializers

from .models import Blog, Tag

class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = "__all__"
