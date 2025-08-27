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

from api.people.serializers.country_region_serializer import (
    CountryRegionSerializer
)
from api.people.models.country_region_model import CountryRegion

logger = logging.getLogger(__name__)


class CountryRegionViewSet(viewsets.ModelViewSet):
    """
    tba
    """
    queryset = CountryRegion.objects.all()  # pylint: disable=no-member
    serializer_class = CountryRegionSerializer
    lookup_field = 'country_region_code'
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'put',
                         'patch', 'delete', 'head', 'options']
    swagger_tags = ['Addresses']

    success_response = {
        200: openapi.Response("OK: The request was successfully received,"
                              "understood, and processed by the server.",
                              CountryRegionSerializer),
    }
    responses = {**success_response, **error_responses}

    @swagger_auto_schema(
        security=[{'Bearer': []}],
        operation_description="Retrieve a list of all CountryRegion records,"
        "including total count and serialized details.",
        operation_id="list",
        operation_summary="Get all country regions",
        responses=responses,
    )
    def list(self, request, *args, **kwargs):
        """
        tba
        """
        # gets the queryset
        queryset = self.get_queryset()

        # check permissions: object can be accessed by the user
        self.check_object_permissions(self.request, queryset)

        # serialize data
        serializer = self.get_serializer(queryset, many=True)
        logging.info("SUCCESS: retrieved list -- %s", serializer.data)

        return Response({
            'count': queryset.count(),
            'data': serializer.data
        }, status=status.HTTP_200_OK)

    success_response = {
        200: openapi.Response("OK: The request was successfully received,"
                              "understood, and processed by the server.",
                              CountryRegionSerializer),
    }
    responses = {**success_response, **error_responses}

    @swagger_auto_schema(
        security=[{'Bearer': []}],
        operation_description="Fetch a single CountryRegion record by its"
        "unique ID. Returns serialized data.",
        operation_id="retrieve",
        operation_summary="Get an country region",
        responses=responses
    )
    def retrieve(self, request, *args, **kwargs):
        """
        tba
        """
        # get CountryRegion instance
        instance = get_object_or_404(
            CountryRegion,
            country_region_code=kwargs['country_region_code'])

        # check permissions: object can be accessed by the user
        self.check_object_permissions(self.request, instance)

        # serialize data
        serializer = self.get_serializer(instance)
        logging.info("SUCCESS: retrieved record -- %s", serializer.data)

        return Response({
            'count': 1,
            'data': serializer.data
        }, status=status.HTTP_200_OK)

    success_response = {
        201: openapi.Response("CREATED: The request was successful and"
                              "resulted in the creation of a new resource.",
                              CountryRegionSerializer),
    }
    responses = {**success_response, **error_responses}

    @swagger_auto_schema(
        security=[{'Bearer': []}],
        operation_description="Create a new CountryRegion record."
        "Client-supplied ID fields are ignored.",
        operation_id="create",
        operation_summary="Create an country region",
        request_body=CountryRegionSerializer,
        responses=responses
    )
    def create(self, request, *args, **kwargs) -> CountryRegion:
        """
        tba
        """
        # check permissions: object can be accessed by the user
        self.check_object_permissions(self.request, request.data)

        # serialize data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        logging.info("SUCCESS: created -- %s", serializer.data)

        return Response({
            'data': serializer.data
            }, status=status.HTTP_201_CREATED)

    success_response = {
        200: openapi.Response("OK: The request was successfully received,"
                              "understood, and processed by the server.",
                              CountryRegionSerializer),
    }
    responses = {**success_response, **error_responses}

    @swagger_auto_schema(
        security=[{'Bearer': []}],
        operation_description="Fully replace an existing CountryRegion"
        "record. All fields except ID are overwritten.",
        operation_id="update",
        operation_summary="Update an country region",
        request_body=CountryRegionSerializer,
        responses=responses
    )
    def update(self, request, *args, **kwargs) -> CountryRegion:
        """
        tba
        """
        instance = get_object_or_404(
            CountryRegion,
            country_region_code=kwargs['country_region_code'])

        # check permissions: object can be accessed by the user
        self.check_object_permissions(self.request, instance)

        # serialize data
        serializer = self.get_serializer(
            instance,
            data=request.data,
            partial=False)

        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        logging.info("SUCCESS: updated -- %s", serializer.data)

        return Response({
            'data': serializer.data
            }, status=status.HTTP_200_OK)

    success_response = {
        200: openapi.Response("OK: The request was successfully received,"
                              "understood, and processed by the server.",
                              CountryRegionSerializer),
    }
    responses = {**success_response, **error_responses}

    @swagger_auto_schema(
        security=[{'Bearer': []}],
        operation_id="partial_update",
        operation_description="Apply partial updates to an CountryRegion"
        "record. Only specified fields are modified. ID field is excluded.",
        operation_summary="Partially update an country region",
        request_body=CountryRegionSerializer,
        responses=responses
    )
    def partial_update(self, request, *args, **kwargs) -> CountryRegion:
        """
        tba
        """

        instance = get_object_or_404(
            CountryRegion,
            country_region_code=kwargs['country_region_code'])
        # check permissions: object can be accessed by the user
        self.check_object_permissions(self.request, instance)
        # serialize data
        serializer = self.get_serializer(instance,
                                         data=request.data,
                                         partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        logging.info("SUCCESS: updated -- %s", serializer.data)

        return Response({
            'data': serializer.data
            }, status=status.HTTP_200_OK)

    success_response = {
        204: openapi.Response("NO CONTENT: The server successfully processed"
                              "the request, but there is no content to return"
                              "in the response body.",
                              CountryRegionSerializer),
    }
    responses = {**success_response, **error_responses}

    @swagger_auto_schema(
        operation_id="destroy",
        operation_summary="Delete an country region",
        operation_description="Delete an CountryRegion record by ID."
        "Requires admin privileges. Returns 204 No Content on success.",
        request_body=CountryRegionSerializer,
        security=[{'Bearer': []}],
        responses=responses
    )
    def destroy(self, request, *args, **kwargs) -> Response:
        """
        tba
        """
        instance = get_object_or_404(
            CountryRegion,
            country_region_code=kwargs['country_region_code'])
        # check permissions: object can be accessed by the user
        self.check_object_permissions(self.request, instance)

        instance.delete()

        logging.info("SUCCESS: country region deleted -- %s", instance.name)

        return Response(status=status.HTTP_204_NO_CONTENT)

    responses = {**success_response, **error_responses}

    @swagger_auto_schema(
        operation_id="options",
        operation_summary="Retrieve metadata for CountryRegion endpoints.",
        operation_description="Return metadata for CountryRegion endpoints,"
        "including allowed methods and request formats."
        "Used by clients for discovery.",
        request_body=CountryRegionSerializer,
        security=[{'Bearer': []}],
        responses=responses
    )
    def options(self, request, *args, **kwargs):
        """
        tba
        """

        data = {
            "name": "country regions",
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
                                description='Total number of country regions'
                                'available'
                            )
                        }
                    )
    }

    responses = {**success_response, **error_responses}

    @swagger_auto_schema(
        operation_id="head",
        operation_summary="Retrieve metadata headers for country regions",
        operation_description=(
            "Returns HTTP headers without a response body. Useful for checking"
            "resource availability, supported methods, and total count of"
            "country regions. Requires admin authentication via Bearer token."
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
    def head(self):  # pylint: disable=method-hidden
        """
        tba
        """
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
