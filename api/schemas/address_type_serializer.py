"""
AddressType Serializer Module

This module defines the `AddressTypeSerializer`, a Django REST Framework (DRF)
serializer for the `AddressType` model. It enables API consumers to interact
with address type data in a structured, validated format. The serializer
exposes all model fields while marking system-managed fields as read-only
to preserve data integrity.

Key Features:
- Full model serialization via `fields = '__all__'`
- Read-only enforcement on `address_type_id`, `rowguid`, and `modified_date`
- OpenAPI-compatible field documentation via DRF's introspection
- Supports partial updates and integration with Create/Update views

Intended Use:
- Used in DRF views to expose address type metadata for filtering,
categorization, or external system mapping
- Ideal for onboarding workflows, admin interfaces, and legacy DB integration

Notes:
- Extend with custom validation or field-level help_text for enhanced Swagger
docs
- Consider adding `extra_kwargs` for write-only or required fields if needed
"""


from rest_framework import serializers
from rest_framework.reverse import reverse
from api.models.address_type_model import AddressType
from api.utils.hateoas_mixin import HATEOASMixin


class AddressTypeSerializer(HATEOASMixin, serializers.ModelSerializer):
    """
    Serializer for the AddressType model.

    This class transforms `AddressType` instances into JSON-compatible
    representations for API responses and validates incoming data for creation
    or updates. It exposes all fields while marking system-managed fields as
    read-only to preserve integrity.

    Features:
        - Serializes all model fields (`fields = '__all__'`)
        - Enforces read-only on `address_type_id`, `rowguid`, and
        `modified_date`
        - Compatible with DRF views for create, retrieve, update, and list
        operations
        - Supports partial updates via PATCH

    Example usage:
        serializer = AddressTypeSerializer(data={"name": "Shipping"})
        serializer.is_valid(raise_exception=True)
        serializer.save()

    Notes:
        - Extend with `extra_kwargs` or custom validators for stricter input
        control
        - Ideal for onboarding workflows and legacy DB integration
    """
    model = AddressType

    class Meta:
        """
        Configuration for AddressTypeSerializer behavior.

        This inner class defines how the serializer interacts with the model
        and which fields are exposed or protected during API operations.

        Attributes:
            model (AddressType): The model being serialized.
            fields (str): Includes all model fields (`'__all__'`).
            read_only_fields (list): Prevents updates to system-managed fields:
                - `address_type_id`: Auto-generated primary key
                - `rowguid`: UUID for external mapping
                - `modified_date`: Auto-updated timestamp

        Notes:
            - Use `extra_kwargs` to define write-only or required fields.
            - Consider field-level `help_text` for enhanced Swagger
            documentation
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
            return reverse(view_name, args=[obj.address_type_id], request=request)
        else:
            return None

    def get_links(self, obj):
        """
        tba
        """
        request = self.context.get("request")

        # Get next object
        next_obj = (
            AddressType.objects.filter(address_type_id__gt=obj.address_type_id)  # pylint: disable=no-member
            .order_by("address_type_id")
            .first()
        )
        # Get previous object
        previous_obj = (
            AddressType.objects.filter(address_type_id__lt=obj.address_type_id)  # pylint: disable=no-member
            .order_by("-address_type_id")
            .first()
        )

        return {
            "next": self.get_object_url(next_obj, "retrieve", request),
            "previous": self.get_object_url(previous_obj, "retrieve", request),

            # GET: retrieve
            "self": {
                "href": reverse("retrieve", args=[obj.address_type_id], request=request),
                "method": "GET"
            },

            # GET: list, POST: create
            "list": {
                "href": reverse("list", request=request),
                "method": "GET"
            },
            "create": {
                "href": reverse("list", request=request),
                "method": "POST"
            },

            # Item-level operations (PUT, PATCH, DELETE)
            "update": {
                "href": reverse("retrieve", args=[obj.address_type_id], request=request),
                "method": "PUT"
            },
            "partial_update": {
                "href": reverse("retrieve", args=[obj.address_type_id], request=request),
                "method": "PATCH"
            },
            "destroy": {
                "href": reverse("retrieve", args=[obj.address_type_id], request=request),
                "method": "DELETE"
            }
        }
