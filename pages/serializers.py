from rest_framework import serializers

from .models import Navigation


class NavigationChildSerializer(serializers.ModelSerializer):
    """
    导航栏子节点序列化
    """

    class Meta:
        model = Navigation
        fields = ('id', 'nav_text', 'nav_url')


class NavigationParentSerializer(serializers.ModelSerializer):
    """
    导航栏父节点序列化
    """
    nav_sub = NavigationChildSerializer(many=True)

    class Meta:
        model = Navigation
        fields = ('id', 'nav_img', 'nav_text', 'nav_sub', 'has_submenu', 'nav_url')