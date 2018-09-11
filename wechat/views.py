from django.shortcuts import render

from rest_framework import mixins, viewsets
from rest_framework.response import Response

from .serializers import UserSerializer
from .models import User, USER_POSITION, SIGN_USER_CHOICES


class UserViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        user = User()
        user.username = data["username"]
        user.wechat_username = data["wechat_username"]
        user.realname = data["realname"]
        user.birth = data["birth"]
        user.user_tag = data["user_tag"]
        user.position = data["position"]
        user.save()
        return Response({"status": "success"})

    def list(self, request, *args, **kwargs):

        return Response({"result": USER_POSITION})
