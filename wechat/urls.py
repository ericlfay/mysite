# coding: utf-8
# @Author: ericlfay
# @Date:   2018-09-10 15:11:50

from django.urls import path, include
from rest_framework.routers import DefaultRouter


from .views import UserViewSet, UserInfoSet


router = DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'userinfo', UserInfoSet)


urlpatterns = [
    path('', include(router.urls)),
]
