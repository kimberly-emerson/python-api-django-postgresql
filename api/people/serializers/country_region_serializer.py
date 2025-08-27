"""
tba
"""

from rest_framework import serializers
from rest_framework.reverse import reverse
from api.people.models.country_region_model import CountryRegion
from api.utils.hateoas_mixin import HATEOASMixin


class CountryRegionSerializer(HATEOASMixin, serializers.ModelSerializer):
    """
    tba
    """
    model = CountryRegion

    class Meta:
        """
        tba
        """

        model = CountryRegion
        fields = '__all__'
        read_only_fields = [
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
                args=[obj.country_region_code],
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
            CountryRegion.objects.filter(  # pylint: disable=no-member
                country_region_code__gt=obj.country_region_code)
            .order_by("country_region_code")
            .first()
        )
        # Get previous object
        previous_obj = (
            CountryRegion.objects.filter(  # pylint: disable=no-member
                country_region_code__lt=obj.country_region_code
            )
            .order_by("-country_region_code")
            .first()
        )

        return {
            "next": self.get_object_url(next_obj, "retrieve", request),
            "previous": self.get_object_url(previous_obj, "retrieve", request),

            # GET: retrieve
            "self": {
                "href": reverse("retrieve",
                                args=[obj.country_region_code],
                                request=request),
                "method": "GET"
            },

            # GET: list
            # POST: create
            # OPTIONS
            # HEAD
            "list": {
                "href": reverse("list", request=request),
                "method": "GET"
            },
            "create": {
                "href": reverse("list", request=request),
                "method": "POST"
            },
            "options": {
                "href": reverse("list", request=request),
                "method": "OPTIONS"
            },
            "head": {
                "href": reverse("list", request=request),
                "method": "HEAD"
            },

            # PUT: update
            # PATCH: partial_update
            # DELETE: destroy
            "update": {
                "href": reverse("retrieve",
                                args=[obj.country_region_code],
                                request=request),
                "method": "PUT"
            },
            "partial_update": {
                "href": reverse("retrieve",
                                args=[obj.country_region_code],
                                request=request),
                "method": "PATCH"
            },
            "destroy": {
                "href": reverse("retrieve",
                                args=[obj.country_region_code],
                                request=request),
                "method": "DELETE"
            },
        }
