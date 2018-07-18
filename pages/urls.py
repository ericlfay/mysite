from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import NavigationListSet

router = DefaultRouter()
router.register(r'nav', NavigationListSet)
urlpatterns = [
    path('', include(router.urls)),
]
