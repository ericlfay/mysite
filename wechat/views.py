import logging
import requests

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler("./log.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

from django.shortcuts import render

from rest_framework import mixins, viewsets
from rest_framework.response import Response

from .serializers import UserSerializer
from .models import User, USER_POSITION, SIGN_USER_CHOICES, RealUser


class UserViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            user = User()
            logger.info(data)
            user.openid = data['openid']
            user.username = data['username']
            user.wechat_username = data['wechat_username']
            user.realname = data['realname']
            user.birth = data['birth']
            user.user_tag = data['user_tag']
            user.position = data['position']
            user.save()
            logger.info(user)
            return Response({"status": "success"})
        except Exception as e:
            logger.error(e)

    def list(self, request, *args, **kwargs):
        user = None
        openid = self.request.GET.get('openid', "")
        realuser = RealUser.objects.all()
        if openid:
            user = User.objects.filter(openid=openid)
        result = []
        if user:
            return Response({"has_user": "yes"})
        else:
            for user in realuser:
                result.append(user.realname)
            return Response({"has_user": "no",
                             "result": USER_POSITION,
                             "realname": result})


class UserInfoSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):

        code = self.request.GET.get('code', "")
        url = "https://api.weixin.qq.com/sns/jscode2session"
        appid = "wxe964682782f4efc5"
        secret = "aabafb983329de4cf9f81e1f52cf941f"
        grant_type = "authorization_code"
        openid = requests.get(url=url,
                              params={'appid': appid,
                                      "secret": secret,
                                      "js_code": code,
                                      "grant_type": grant_type})
        logger.error({"result": openid.text})
        return Response(openid.json())

