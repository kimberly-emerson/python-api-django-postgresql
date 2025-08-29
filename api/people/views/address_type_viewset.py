"""
tba
"""

import logging
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_standardized_errors.handler import exception_handler
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from api.config.swagger import error_responses

from api.people.models.address_type_model import AddressType
from api.people.serializers.address_type_serializer import (
    AddressTypeSerializer
)

logger = logging.getLogger(__name__)


class AddressTypeViewSet(viewsets.ModelViewSet):
    """
    tba
    """
    # pylint: disable=no-member
    queryset = AddressType.objects.all()
    serializer_class = AddressTypeSerializer
    lookup_field = 'address_type_id'
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'patch', 'delete',
                         'head', 'options']
    swagger_tags = ['Addresses']

    success_response = {
        200: openapi.Response("OK: The request was successfully received,"
                              "understood, and processed by the server.",
                              AddressTypeSerializer),
    }
    responses = {**success_response, **error_responses}

    @swagger_auto_schema(
        security=[{'Bearer': []}],
        operation_description="Retrieve a list of all AddressType records,"
        "including total count and serialized details.",
        operation_id="list",
        operation_summary="Get all address types",
        responses=responses,
    )
    def list(self, request, *args, **kwargs):
        """
        tba
        """

        logging.info("GET request received for %s", request)

        # gets the queryset
        queryset = self.get_queryset()

        # check permissions: object can be accessed by the user
        self.check_object_permissions(self.request, queryset)

        # serialize data
        serializer = self.get_serializer(queryset, many=True)

        return Response({
            'count': queryset.count(),
            'data': serializer.data
        }, status=status.HTTP_200_OK)

    success_response = {
        200: openapi.Response("OK: The request was successfully received,"
                              "understood, and processed by the server.",
                              AddressTypeSerializer),
    }
    responses = {**success_response, **error_responses}

    @swagger_auto_schema(
        security=[{'Bearer': []}],
        operation_description="Fetch a single AddressType record by its"
        "unique ID. Returns serialized data.",
        operation_id="retrieve",
        operation_summary="Get an address type",
        responses=responses
    )
    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve a single AddressType record by ID.

        Fetches a specific AddressType instance identified by
        `address_type_id`.

        Parameters
        ----------
        request : Request
            The HTTP request object.
        *args : tuple
            Additional positional arguments.
        **kwargs : dict
            Must include `address_type_id`.

        Returns
        -------
        Response
            JSON response containing:
            - `count`: always 1
            - `data`: serialized AddressType record
        """

        logging.info("GET request received for %s", request)

        # get AddressType instance
        instance = get_object_or_404(
            AddressType,
            address_type_id=kwargs['address_type_id'])

        # check permissions: object can be accessed by the user
        self.check_object_permissions(self.request, instance)

        # serialize data
        serializer = self.get_serializer(instance)

        return Response({
            'count': 1,
            'data': serializer.data
        }, status=status.HTTP_200_OK)

    success_response = {
        201: openapi.Response("CREATED: The request was successful and"
                              "resulted in the creation of a new resource.",
                              AddressTypeSerializer),
    }
    responses = {**success_response, **error_responses}

    @swagger_auto_schema(
        security=[{'Bearer': []}],
        operation_description="Create a new AddressType record."
        "Client-supplied ID fields are ignored.",
        operation_id="create",
        operation_summary="Create an address type",
        request_body=AddressTypeSerializer,
        responses=responses
    )
    def create(self, request, *args, **kwargs) -> AddressType:
        """
        Create a new AddressType record.

        Ignores any client-supplied `address_type_id` and generates a new one.

        Parameters
        ----------
        request : Request
            The HTTP request object containing AddressType data.
        *args : tuple
            Additional positional arguments.
        **kwargs : dict
            Additional keyword arguments.

        Returns
        -------
        Response
            JSON response containing the newly created AddressType data
            and HTTP status 201 Created.
        """

        logging.info("POST request received for %s", request)

        # check permissions: object can be accessed by the user
        self.check_object_permissions(self.request, request.data)

        # serialize data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'data': serializer.data
            }, status=status.HTTP_201_CREATED)

    success_response = {
        200: openapi.Response("OK: The request was successfully received,"
                              "understood, and processed by the server.",
                              AddressTypeSerializer),
    }
    responses = {**success_response, **error_responses}

    @swagger_auto_schema(
        security=[{'Bearer': []}],
        operation_description="Fully replace an existing AddressType"
        "record. All fields except ID are overwritten.",
        operation_id="update",
        operation_summary="Update an address type",
        request_body=AddressTypeSerializer,
        responses=responses
    )
    def update(self, request, *args, **kwargs) -> AddressType:
        """
        Fully update an existing AddressType record.

        Replaces all fields of an AddressType instance except the primary key
        (`address_type_id`).

        Parameters
        ----------
        request : Request
            The HTTP request object containing updated AddressType data.
        *args : tuple
            Additional positional arguments.
        **kwargs : dict
            Must include `address_type_id`.

        Returns
        -------
        Response
            JSON response containing updated AddressType data and
            HTTP status 200 OK.
        """

        logging.info("PUT request received for %s", request)

        instance = get_object_or_404(
            AddressType,
            address_type_id=kwargs['address_type_id'])

        # check permissions: object can be accessed by the user
        self.check_object_permissions(self.request, instance)

        # serialize data
        serializer = self.get_serializer(
            instance,
            data=request.data,
            partial=False)

        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response({
            'data': serializer.data
            }, status=status.HTTP_200_OK)

    success_response = {
        200: openapi.Response("OK: The request was successfully received,"
                              "understood, and processed by the server.",
                              AddressTypeSerializer),
    }
    responses = {**success_response, **error_responses}

    @swagger_auto_schema(
        security=[{'Bearer': []}],
        operation_id="partial_update",
        operation_description="Apply partial updates to an AddressType"
        "record. Only specified fields are modified. ID field is excluded.",
        operation_summary="Partially update an address type",
        request_body=AddressTypeSerializer,
        responses=responses
    )
    def partial_update(self, request, *args, **kwargs) -> AddressType:
        """
        Partially update an AddressType record.

        Updates only the fields included in the request payload. The
        primary key (`address_type_id`) cannot be modified.

        Parameters
        ----------
        request : Request
            The HTTP request object containing fields to update.
        *args : tuple
            Additional positional arguments.
        **kwargs : dict
            Must include `address_type_id`.

        Returns
        -------
        Response
            JSON response containing updated AddressType data and
            HTTP status 200 OK.
        """
        logging.info("PATCH request received for %s", request)

        instance = get_object_or_404(
            AddressType,
            address_type_id=kwargs['address_type_id'])
        # check permissions: object can be accessed by the user
        self.check_object_permissions(self.request, instance)
        # serialize data
        serializer = self.get_serializer(instance,
                                         data=request.data,
                                         partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response({
            'data': serializer.data
            }, status=status.HTTP_200_OK)

    success_response = {
        204: openapi.Response("NO CONTENT: The server successfully processed"
                              "the request, but there is no content to return"
                              "in the response body.",
                              AddressTypeSerializer),
    }
    responses = {**success_response, **error_responses}

    @swagger_auto_schema(
        operation_id="destroy",
        operation_summary="Delete an address type",
        operation_description="Delete an AddressType record by ID."
        "Requires admin privileges. Returns 204 No Content on success.",
        request_body=AddressTypeSerializer,
        security=[{'Bearer': []}],
        responses=responses
    )
    def destroy(self, request, *args, **kwargs) -> Response:
        """
        Delete an AddressType record by ID.

        Removes the specified AddressType instance. Requires elevated
        (admin) privileges.

        Parameters
        ----------
        request : Request
            The HTTP request object.
        *args : tuple
            Additional positional arguments.
        **kwargs : dict
            Must include `address_type_id`.

        Returns
        -------
        Response
            Empty response with HTTP status 204 No Content.
        """
        logging.info("DELETE request received for %s", request)

        instance = get_object_or_404(
            AddressType,
            address_type_id=kwargs['address_type_id'])
        # check permissions: object can be accessed by the user
        self.check_object_permissions(self.request, instance)

        instance.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    responses = {**success_response, **error_responses}

    @swagger_auto_schema(
        operation_id="options",
        operation_summary="Retrieve metadata for AddressType endpoints.",
        operation_description="Return metadata for AddressType endpoints,"
        "including allowed methods and request formats."
        "Used by clients for discovery.",
        request_body=AddressTypeSerializer,
        security=[{'Bearer': []}],
        responses=responses
    )
    def options(self, request, *args, **kwargs):
        """
        Retrieve metadata for AddressType endpoints.

        Provides information on available HTTP methods, request formats,
        and a description of the resource.

        Parameters
        ----------
        request : Request
            The HTTP request object.
        *args : tuple
            Additional positional arguments.
        **kwargs : dict
            Additional keyword arguments.

        Returns
        -------
        Response
            JSON response containing:
            - `name`: resource name
            - `description`: description of AddressType resource
            - `allowed_methods`: list of supported HTTP methods
        """
        logging.info("OPTIONS request received for %s", request)

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

    success_response = {
        200: openapi.Response(
                        description="Headers only, no body",
                        headers={
                            'Accept': openapi.Schema(
                                type=openapi.TYPE_STRING,
                                description='Response accept'
                                '(application/json)'
                            ),
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
                    )
    }

    responses = {**success_response, **error_responses}

    @swagger_auto_schema(
        operation_id="head",
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
        responses=responses,
        security=[{'Bearer': []}]
    )
    def head(self, request):  # pylint: disable=method-hidden
        """
        Retrieve metadata headers for the AddressType endpoint.

        Returns only HTTP headers without a response body. Useful for
        checking resource availability, supported methods, and total count.

        Returns
        -------
        Response
            Response with headers:
            - `Content-Type`: response content type
            - `Authorization`: required auth header
            - `Allow`: supported methods
            - `X-Total-Count`: total number of address types
        """
        logging.info("HEAD request received for %s", request)

        total_count = self.get_queryset().count()
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer <access_token>',
            'Allow': 'GET, POST, PUT, PATCH, DELETE, OPTIONS, HEAD',
            'X-Total-Count': str(total_count)
        }
        return Response(headers=headers, status=status.HTTP_200_OK)

    def get_exception_handler(self):
        """
        Get the exception handler for this viewset.

        Uses `drf_standardized_errors` to produce consistent error
        responses across the API.

        Returns
        -------
        function
            Exception handler function.
        """
        return exception_handler
