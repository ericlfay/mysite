# -*- coding: utf-8 -*-
# @Author: ericlfay
# @Date:   2018-07-23 15:24:06
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import BlogListSet

router = DefaultRouter()
router.register(r'blogs', BlogListSet)
urlpatterns = [
    path('', include(router.urls)),
]
