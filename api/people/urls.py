"""
tba
"""

from django.urls import path
from api.people.views.address_type_viewset import AddressTypeViewSet

urlpatterns = [
     # AddressType
     path(
        "/address-types",
        AddressTypeViewSet.as_view({
            "get": "list",
            "post": "create",
        }),
        name="list",
        ),
     path(
        "/address-types/<int:address_type_id>",
        AddressTypeViewSet.as_view({
            "get": "retrieve",
            "patch": "partial_update",
            "put": "update",
            "delete": "destroy",
        }),
        name="retrieve",
        ),

]
