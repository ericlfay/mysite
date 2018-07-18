from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins, viewsets
from .models import Navigation
from .serializers import NavigationParentSerializer

class NavigationListSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    导航栏 父节点
    """
    # permission_classes = (IsAuthenticated,)
    queryset = Navigation.objects.filter(nav_parent=None)
    serializer_class = NavigationParentSerializer