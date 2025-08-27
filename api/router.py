"""
tba
"""

from rest_framework.routers import DefaultRouter

from api.admin.views.user_viewset import UserViewSet
from api.admin.views.group_viewset import GroupViewSet


router = DefaultRouter()

router.register(r'users', UserViewSet, basename='user')
router.register(r'groups', GroupViewSet, basename='group')
