"""
tba
"""

from rest_framework import serializers
from rest_framework.reverse import reverse
from api.people.models.address_type_model import AddressType
from api.utils.hateoas_mixin import HATEOASMixin


class AddressTypeSerializer(HATEOASMixin, serializers.ModelSerializer):
    """
    tba
    """
    model = AddressType

    class Meta:
        """
        tba
        """

        model = AddressType
        fields = '__all__'
        read_only_fields = [
            'address_type_id',
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
                args=[obj.address_type_id],
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
            AddressType.objects.filter(  # pylint: disable=no-member
                address_type_id__gt=obj.address_type_id)
            .order_by("address_type_id")
            .first()
        )
        # Get previous object
        previous_obj = (
            AddressType.objects.filter(  # pylint: disable=no-member
                address_type_id__lt=obj.address_type_id
            )
            .order_by("-address_type_id")
            .first()
        )

        return {
            "next": self.get_object_url(next_obj, "retrieve", request),
            "previous": self.get_object_url(previous_obj, "retrieve", request),

            # GET: retrieve
            "self": {
                "href": reverse("retrieve",
                                args=[obj.address_type_id],
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
                                args=[obj.address_type_id],
                                request=request),
                "method": "PUT"
            },
            "partial_update": {
                "href": reverse("retrieve",
                                args=[obj.address_type_id],
                                request=request),
                "method": "PATCH"
            },
            "destroy": {
                "href": reverse("retrieve",
                                args=[obj.address_type_id],
                                request=request),
                "method": "DELETE"
            },
        }
