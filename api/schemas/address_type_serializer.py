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
from api.models.address_type_model import AddressType


class AddressTypeSerializer(serializers.ModelSerializer):
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
