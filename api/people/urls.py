"""
tba
"""

from django.urls import path

from api.people.views.address_type_viewset import AddressTypeViewSet
from api.people.views.country_region_viewset import CountryRegionViewSet


urlpatterns = [
     # AddressType
     path(
        "/address-types",
        AddressTypeViewSet.as_view({
            "get": "list",
            "post": "create",
        }),
        name="address-types",
        ),
     path(
        "/address-types/<int:address_type_id>",
        AddressTypeViewSet.as_view({
            "get": "retrieve",
            "patch": "partial_update",
            "put": "update",
            "delete": "destroy",
        }),
        name="address-types-id",
        ),

     # CountryRegion
     path(
        "/country-regions",
        CountryRegionViewSet.as_view({
            "get": "list",
            "post": "create",
        }),
        name="country-regions",
        ),
     path(
        "/country-regions/<str:country_region_code>",
        CountryRegionViewSet.as_view({
            "get": "retrieve",
            "patch": "partial_update",
            "put": "update",
            "delete": "destroy",
        }),
        name="country-regions-code",
        ),
]
