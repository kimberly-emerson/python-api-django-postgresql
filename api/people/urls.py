"""
tba
"""

from django.urls import path

from api.people.views.address_type_viewset import AddressTypeViewSet
from api.people.views.country_region_viewset import CountryRegionViewSet
from api.people.views.state_province_viewset import StateProvinceViewSet


urlpatterns = [
     # AddressType
     path(
        "/address-types",
        AddressTypeViewSet.as_view({
            "get": "list",
            "post": "create",
            "options": "options",
            "head": "head"
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
            "options": "options",
            "head": "head"
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
     # StateProvince
     path(
        "/state-provinces",
        StateProvinceViewSet.as_view({
            "get": "list",
            "post": "create",
            "options": "options",
            "head": "head"
        }),
        name="state-provinces",
        ),
     path(
        "/state-provinces/<int:address_type_id>",
        StateProvinceViewSet.as_view({
            "get": "retrieve",
            "patch": "partial_update",
            "put": "update",
            "delete": "destroy",
        }),
        name="state-provinces-id",
        ),
]
