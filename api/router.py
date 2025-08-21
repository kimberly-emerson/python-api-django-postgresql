"""
DRF Router Configuration

Configures the DRF router for views and viewsets, enabling RESTful routing
for metadata management. This endpoint supports full CRUD
operations and is restricted to authenticated admin users.

Registered endpoints:
    /api/address-types/

ViewSets:
    AddressTypeViewSet

Permissions:
    - IsAuthenticated
    - Requires Bearer token in Authorization header

Methods:
    GET, POST, PUT, PATCH, DELETE, OPTIONS

Usage:
    Include this router in the `api/urls.py`
"""

from rest_framework.routers import DefaultRouter
from api.views.address_type_viewset import AddressTypeViewSet

router = DefaultRouter()
router.register(r'address-types',
                AddressTypeViewSet,
                basename='address-type')
