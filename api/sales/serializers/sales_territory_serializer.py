"""
tba
"""

from rest_framework import serializers
from rest_framework.reverse import reverse

from api.people.models.country_region_model import CountryRegion
from api.sales.models.sales_territory_model import SalesTerritory
from api.people.serializers.country_region_serializer import (
  CountryRegionSerializer
)


class SalesTerritorySerializer(serializers.ModelSerializer):
    """
    tba
    """
    model = SalesTerritory
    # Write-only: accept country_region_code when creating/updating
    country_region_code = serializers.SlugRelatedField(
        slug_field="country_region_code",
        queryset=CountryRegion.objects.all(),
        source="country_region",
        write_only=True
    )

    # Read-only: return nested country_region detail
    country_region_detail = CountryRegionSerializer(
        source="country_region",
        read_only=True
    )

    class Meta:
        """
        tba
        """

        model = SalesTerritory
        fields = [
            "sales_territory_id",
            "name",
            "region",
            "sales_ytd",
            "sales_last_year",
            "cost_ytd",
            "cost_last_year",
            "country_region_code",
            "country_region_detail"
        ]
        read_only_fields = [
            'sales_territory_id',
            'rowguid',
            'modified_date',
        ]

    def get_object_url(self, obj, view_name: str, request):
        """
        Returns the reverse URL for a given object and view name, or None
        if the object is None.
        """
        if obj:
            return reverse(
                view_name,
                args=[obj.state_province_id],
                request=request)
        else:
            return None

    def get_links(self, obj):
        """
        tba
        """
        request = self.context.get("request")

        # Get next object
        next_obj = (
            StateProvince.objects.filter(  # pylint: disable=no-member
                state_province_id__gt=obj.state_province_id)
            .order_by("state_province_id")
            .first()
        )
        # Get previous object
        previous_obj = (
            StateProvince.objects.filter(  # pylint: disable=no-member
                state_province_id__lt=obj.state_province_id
            )
            .order_by("-state_province_id")
            .first()
        )

        return {
            "next": self.get_object_url(
                next_obj,
                "address-types-id",
                request
            ),

            "previous": self.get_object_url(
                previous_obj,
                "address-types-id",
                request
            ),

            # GET: retrieve
            "self": {
                "href": reverse("address-types-id",
                                args=[obj.state_province_id],
                                request=request),
                "method": "GET"
            },

            # GET: list
            # POST: create
            # OPTIONS
            # HEAD
            "list": {
                "href": reverse("address-types", request=request),
                "method": "GET"
            },
            "create": {
                "href": reverse("address-types", request=request),
                "method": "POST"
            },
            "options": {
                "href": reverse("address-types", request=request),
                "method": "OPTIONS"
            },
            "head": {
                "href": reverse("address-types", request=request),
                "method": "HEAD"
            },

            # PUT: update
            # PATCH: partial_update
            # DELETE: destroy
            "update": {
                "href": reverse("address-types-id",
                                args=[obj.state_province_id],
                                request=request),
                "method": "PUT"
            },
            "partial_update": {
                "href": reverse("address-types-id",
                                args=[obj.state_province_id],
                                request=request),
                "method": "PATCH"
            },
            "destroy": {
                "href": reverse("address-types-id",
                                args=[obj.state_province_id],
                                request=request),
                "method": "DELETE"
            },
        }
