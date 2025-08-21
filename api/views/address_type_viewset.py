"""
Address Type ViewSet Module

This module defines a secured Django REST Framework (DRF) `ModelViewSet` for
managing address type records via RESTful API endpoints. It supports full CRUD
operations and is integrated with Swagger documentation via `drf_yasg`.

Permissions:
- Requires authentication (`IsAuthenticated`)
- Secured with Bearer token in Swagger UI

Supported HTTP Methods:
- GET (list, retrieve)
- POST (create)
- PUT (update)
- PATCH (partial_update)
- DELETE (destroy)
- OPTIONS, HEAD

Swagger Integration:
Each method includes `swagger_auto_schema` decorators for:
- Operation summaries and descriptions
- Security schemes
- Response schemas and status codes

ViewSet Features:
- `list`: Returns all address types with count and serialized data
- `retrieve`: Returns a single address type by `address_type_id`
- `create`: Accepts validated input and ignores client-supplied ID
- `update`: Replaces an address type, excluding ID field
- `partial_update`: Applies partial changes, excluding ID field
- `destroy`: Deletes an address type (admin-only)
- `options`: Returns custom metadata for OPTIONS requests

Notes:
- Uses `AddressTypeSerializer` for validation and serialization
- Enforces read-only fields: `address_type_id`, `rowguid`, `modified_date`
- Ideal for admin dashboards, onboarding workflows, and legacy DB integration
"""

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from api.models.address_type_model import AddressType
from api.schemas.address_type_serializer import AddressTypeSerializer


class AddressTypeViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing AddressType records via RESTful API endpoints.

    This class provides full CRUD operations (`list`, `retrieve`, `create`,
    `update`, `partial_update`, `destroy`) for the `AddressType` model,
    secured by authentication and admin-only access. It integrates with
    Swagger via `drf_yasg` decorators for rich API documentation.

    Features:
        - Secured with `IsAuthenticated` and `IsAdminUser` permissions
        - Supports Bearer token authentication in Swagger UI
        - Custom Swagger tags for grouped documentation ("Addresses")
        - Explicitly defines allowed HTTP methods for clarity and control

    Methods:
        - `list`: Returns all address types with count and serialized data
        - `retrieve`: Returns a single address type by ID
        - `create`: Creates a new address type, ignoring client-supplied ID
        - `update`: Replaces an address type, excluding ID field
        - `partial_update`: Applies partial changes, excluding ID field
        - `destroy`: Deletes an address type (admin-only)
        - `options`: Returns custom metadata for OPTIONS requests

    Notes:
        - Uses `AddressTypeSerializer` for validation and serialization
        - Ideal for admin dashboards, onboarding workflows, and legacy DB
        integration
        - Swagger decorators provide operation summaries, descriptions, and
        response schemas
    """

    queryset = AddressType.objects.all()  # pylint: disable=no-member
    serializer_class = AddressTypeSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'put',
                         'patch', 'delete', 'head', 'options']
    swagger_tags = ['Addresses']

    @swagger_auto_schema(
        security=[{'Bearer': []}],
        operation_description="Retrieve a list of all AddressType records,"
        "including total count and serialized details.",
        operation_id="list",
        operation_summary="Get all address types",
        responses={
            200: openapi.Response("Address types retrieved successfully",
                                  AddressTypeSerializer),
            401: "User not authorized."
        }
    )
    def list(self, request, *args, **kwargs):
        """
        Returns a list of all AddressType records.

        Includes total count and serialized data.
        """
        # gets the queryset
        queryset = self.get_queryset()
        # serialize data
        serializer = self.get_serializer(queryset, many=True)

        return Response({
            'count': queryset.count(),
            'data': serializer.data
        }, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        security=[{'Bearer': []}],
        operation_description="Fetch a single AddressType record by its"
        "unique ID. Returns serialized data.",
        operation_id="retrieve",
        operation_summary="Get an address type",
        responses={
            200: openapi.Response("Address type retrieved successfully",
                                  AddressTypeSerializer),
            401: "User not authorized."
        }
    )
    def retrieve(self, request, *args, **kwargs):
        """
        Retrieves a single AddressType record by its ID.

        Returns serialized data for the specified object.
        """

        # gets the queryset
        instance = self.get_object()
        # serialize data
        serializer = self.get_serializer(instance, many=True)

        return Response({
            'count': instance.count(),
            'data': serializer.data
        }, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        security=[{'Bearer': []}],
        operation_description="Create a new AddressType record."
        "Client-supplied ID fields are ignored.",
        operation_id="create",
        operation_summary="Create an address type",
        request_body=AddressTypeSerializer,
        responses={
            201: openapi.Response("Address type created successfully",
                                  AddressTypeSerializer),
            401: "User not authorized."
        }
    )
    def create(self, request, *args, **kwargs) -> AddressType:
        """
        Creates a new AddressType record.

        Ignores client-supplied ID fields.
        """

        data = request.data.copy()
        data.pop('address_type_id', None)  # remove 'id' if present
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({
            'data': serializer.data
            }, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        security=[{'Bearer': []}],
        operation_description="Fully replace an existing AddressType"
        "record. All fields except ID are overwritten.",
        operation_id="update",
        operation_summary="Update an address type",
        request_body=AddressTypeSerializer,
        responses={
            200: openapi.Response("Address type updated successfully",
                                  AddressTypeSerializer),
            401: "User not authorized."
        }
    )
    def update(self, request, *args, **kwargs) -> AddressType:
        """
        Fully updates an existing AddressType record.

        Replaces all fields except ID.
        """

        data = request.data.copy()
        data.pop('address_type_id', None)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            'data': serializer.data
            }, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        security=[{'Bearer': []}],
        operation_id="partial_update",
        operation_description="Apply partial updates to an AddressType"
        "record. Only specified fields are modified. ID field is excluded.",
        operation_summary="Partially update an address type",
        request_body=AddressTypeSerializer,
        responses={
            200: openapi.Response("Address type updated successfully",
                                  AddressTypeSerializer),
            401: "User not authorized."
        }
    )
    def partial_update(self, request, *args, **kwargs) -> AddressType:
        """
        Partially updates an AddressType record.

        Applies changes to specified fields only. ID field is excluded.
        """

        data = request.data.copy()
        data.pop('address_type_id', None)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            'data': serializer.data
            }, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        security=[{'Bearer': []}],
        operation_description="Delete an AddressType record by ID."
        "Requires admin privileges. Returns 204 No Content on success.",
        operation_id="destroy",
        operation_summary="Delete an address type",
        request_body=AddressTypeSerializer,
        responses={
            200: openapi.Response("Address type deleted successfully",
                                  AddressTypeSerializer),
            401: "User not authorized."
        }
    )
    def destroy(self, request, *args, **kwargs) -> None:
        """
        Deletes an AddressType record by ID.

        Requires admin privileges. Returns 204 No Content on success.
        """

        instance = self.get_object()
        if not request.user.is_staff:
            return Response({
                'message': 'You do not have permission to delete this item.'
                },
                status=status.HTTP_403_FORBIDDEN)
        self.perform_destroy(instance=instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @swagger_auto_schema(
        operation_description="Return metadata for AddressType endpoints,"
        "including allowed methods and request formats."
        "Used by clients for discovery."
    )
    def options(self, request, *args, **kwargs):
        """
        Returns metadata for AddressType endpoints.

        Used by clients to discover allowed methods and request formats.
        """

        data = {
            "name": "Address Types",
            "description": "Admin-only CRUD interface for managing address"
                           "type metadata (e.g., Billing, Shipping, etc.)",
            "allowed_methods": ["GET", "POST", "PUT",
                                "PATCH", "DELETE", "OPTIONS", "HEAD"],
        }
        return Response({
            'data': data
            }, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Retrieve metadata headers for address types",
        operation_description=(
            "Returns HTTP headers without a response body. Useful for checking"
            "resource availability, supported methods, and total count of"
            "address types. Requires admin authentication via Bearer token."
        ),
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                description='Bearer token for admin authentication',
                required=True,
                type=openapi.TYPE_STRING,
                default='Bearer <access_token>'
            )
        ],
        responses={
                200: openapi.Response(
                    description="Headers only, no body",
                    headers={
                        'Content-Type': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Response content type'
                            '(application/json)'
                        ),
                        'Allow': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Supported HTTP methods'
                        ),
                        'X-Total-Count': openapi.Schema(
                            type=openapi.TYPE_INTEGER,
                            description='Total number of address types'
                            'available'
                        )
                    }
                ),
                401: "Unauthorized – missing or invalid token",
                403: "Forbidden – user lacks admin privileges"
        },
        security=[{'Bearer': []}]
    )
    def head(self):  # pylint: disable=method-hidden
        """
        Handles HEAD requests for the address type endpoint.
        Returns headers indicating resource availability and metadata,
        without a response body.

        Headers include:
            - Content-Type
            - Authorization
            - Allow (supported methods)
            - X-Total-Count (optional: total address types)
        """
        total_count = self.get_queryset().count()
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer <access_token>',
            'Allow': 'GET, POST, PUT, PATCH, DELETE, OPTIONS, HEAD',
            'X-Total-Count': str(total_count)
        }
        return Response(headers=headers, status=status.HTTP_200_OK)
