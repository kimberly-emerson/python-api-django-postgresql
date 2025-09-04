"""
StateProvince API ViewSet.

This module provides a Django REST Framework (DRF) implementation for managing
`StateProvince` resources. It supports standard CRUD operations (list,
retrieve, create, update, partial update, and delete), integrates HATEOAS-style
responses, and extends Swagger schema documentation for better API
discoverability.

Logging:
    All API actions log structured JSON events using `log_event`, which
    ensures:
      - Consistent JSON format for logs.
      - Inclusion of request context (user, method, path, status).
      - Exclusion of sensitive data (only metadata like payload keys logged).
"""

import logging
from typing import Any
from rest_framework import status, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from api.people.models.state_province_model import StateProvince
from api.people.serializers.state_province_serializer import (
    StateProvinceSerializer,
    StateProvinceListResponseSerializer,
    StateProvinceDetailResponseSerializer
)
from api.viewsets.base_hateoas_viewset import BaseHATEOASViewSet
from api.config.build_swagger_schema import build_schema_extension
from api.utils.logging_handler import log_event


logger = logging.getLogger(__name__)


class StateProvincePagination(PageNumberPagination):
    """
    Pagination configuration for StateProvince API endpoints.

    Attributes:
        - page_size (int): Default number of items per page (10).
        - page_size_query_param (str): Query parameter to override the page
        size.
        - max_page_size (int): Maximum allowed page size (100).
    """
    page_size: int = 10
    page_size_query_param: str = 'page_size'
    max_page_size: int = 100


class StateProvinceViewSet(BaseHATEOASViewSet):
    """
    ViewSet for managing StateProvince resources.

    Provides standard CRUD operations along with filtering, ordering,
    authentication, and Swagger schema integration.

    Logging:
        Each method uses `log_event` to record structured JSON logs, including:
          - User performing the action
          - HTTP method and path
          - Resource ID (if applicable)
          - Response status code
    """
    model: str = StateProvince.__name__
    basename: str = 'address-types'
    lookup_field: str = 'state_province_id'
    # pylint: disable=no-member
    queryset = StateProvince.objects.all().order_by(lookup_field)
    serializer_class = StateProvinceSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head',
                         'options']
    swagger_tags = ['Addresses']

    filter_backends = [filters.OrderingFilter]
    ordering_fields = [f'{lookup_field}']
    ordering = [f'{lookup_field}']

    @build_schema_extension(
        model=model,
        operation_id='list',
        serializer=StateProvinceListResponseSerializer,
        success_code=200,
        tags=['Addresses']
    )
    def list(
        self,
        request: Request,
        *args: Any,
        **kwargs: Any
    ) -> Response:
        """
        Retrieve a paginated list of all StateProvince resources.

        Args:
            request (Request): The HTTP request instance.

        Returns:
            Response: A JSON response containing the count and serialized data.

        Logging:
            Logs request context and total count of results.
        """
        log_event(
            "INFO",
            "StateProvince list requested",
            user=str(request.user),
            method=request.method,
            path=request.get_full_path()
        )

        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = StateProvinceSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = StateProvinceSerializer(queryset, many=True)

        log_event(
            "INFO",
            "StateProvince list retrieved",
            user=str(request.user),
            count=len(serializer.data),
            status=status.HTTP_200_OK
        )

        return Response({
            'count': len(serializer.data),
            'data': serializer.data
        }, status=status.HTTP_200_OK)

    @build_schema_extension(
        model=model,
        operation_id='retrieve',
        serializer=StateProvinceDetailResponseSerializer,
        success_code=200,
        tags=['Addresses']
    )
    def retrieve(
        self,
        request: Request,
        *args: Any,
        **kwargs: Any,
    ) -> Response:
        """
        Retrieve a single StateProvince resource by ID.

        Args:
            request (Request): The HTTP request instance.

        Returns:
            Response: A JSON response containing the serialized StateProvince
            data.

        Logging:
            Logs the ID of the retrieved StateProvince and request context.
        """
        instance: StateProvince = self.get_object()
        log_event(
            "INFO",
            "StateProvince retrieved",
            user=str(request.user),
            id=instance.state_province_id,
            method=request.method,
            path=request.get_full_path(),
            status=status.HTTP_200_OK
        )

        serializer = self.get_serializer(instance)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    @build_schema_extension(
        model=model,
        operation_id='create',
        serializer=StateProvinceListResponseSerializer,
        success_code=201,
        tags=['Addresses']
    )
    def create(
        self,
        request: Request,
        *args: Any,
        **kwargs: Any,
    ) -> Response:
        """
        Create a new StateProvince resource.

        Args:
            request (Request): The HTTP request instance containing request
            data.

        Returns:
            Response: A JSON response containing the serialized newly created
            StateProvince.

        Logging:
            Logs payload keys (not sensitive values) and the created
            StateProvince ID.
        """
        log_event(
            "INFO",
            "Create StateProvince request received",
            user=str(request.user),
            method=request.method,
            path=request.get_full_path(),
            payload_keys=list(request.data.keys())
        )

        serializer: StateProvinceSerializer = self.get_serializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        instance: StateProvince = serializer.save()

        log_event(
            "INFO",
            "StateProvince created successfully",
            user=str(request.user),
            id=instance.state_province_id,
            status=status.HTTP_201_CREATED
        )

        return Response(
            {'data': serializer.data},
            status=status.HTTP_201_CREATED
        )

    @build_schema_extension(
        model=model,
        operation_id='update',
        serializer=StateProvinceDetailResponseSerializer,
        success_code=200,
        tags=['Addresses']
    )
    def update(
        self,
        request: Request,
        *args: Any,
        **kwargs: Any,
    ) -> Response:
        """
        Update an existing StateProvince resource.

        Args:
            request (Request): The HTTP request instance containing updated
            data.

        Returns:
            Response: A JSON response containing the updated serialized
            StateProvince.

        Logging:
            Logs the ID being updated, payload keys, and outcome status.
        """
        instance: StateProvince = self.get_object()
        log_event(
            "INFO",
            "Update StateProvince request received",
            user=str(request.user),
            id=instance.state_province_id,
            method=request.method,
            path=request.get_full_path(),
            payload_keys=list(request.data.keys())
        )

        serializer: StateProvinceSerializer = self.get_serializer(
            instance,
            data=request.data,
            partial=False
        )
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        log_event(
            "INFO",
            "StateProvince updated successfully",
            user=str(request.user),
            id=instance.state_province_id,
            status=status.HTTP_200_OK
        )

        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    @build_schema_extension(
        model=model,
        operation_id='update',
        serializer=StateProvinceDetailResponseSerializer,
        success_code=200,
        tags=['Addresses']
    )
    def partial_update(
        self,
        request: Request,
        *args: Any,
        **kwargs: Any,
    ) -> Response:
        """
        Partially update an existing StateProvince resource.

        Args:
            request (Request): The HTTP request instance containing partial
            data.

        Returns:
            Response: A JSON response containing the updated serialized
            StateProvince.

        Logging:
            Logs the ID being patched, payload keys, and outcome status.
        """
        instance: StateProvince = self.get_object()
        log_event(
            "INFO",
            "Partial update request for StateProvince",
            user=str(request.user),
            id=instance.state_province_id,
            method=request.method,
            path=request.get_full_path(),
            payload_keys=list(request.data.keys())
        )

        serializer: StateProvinceSerializer = self.get_serializer(
            instance,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        log_event(
            "INFO",
            "StateProvince partially updated successfully",
            user=str(request.user),
            id=instance.state_province_id,
            status=status.HTTP_200_OK
        )

        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    @build_schema_extension(
        model=model,
        operation_id='destroy',
        serializer=StateProvinceDetailResponseSerializer,
        success_code=204,
        tags=['Addresses']
    )
    def destroy(
        self,
        request: Request,
        *args: Any,
        **kwargs: Any,
    ) -> Response:
        """
        Delete an StateProvince resource.

        Args:
            request (Request): The HTTP request instance.

        Returns:
            Response: An empty response with 204 No Content status.

        Logging:
            Logs the ID being deleted and the outcome status.
        """
        instance: StateProvince = self.get_object()
        log_event(
            "WARNING",
            "Delete StateProvince request received",
            user=str(request.user),
            id=instance.state_province_id,
            method=request.method,
            path=request.get_full_path()
        )

        instance.delete()

        log_event(
            "INFO",
            "StateProvince deleted successfully",
            user=str(request.user),
            id=instance.state_province_id,
            status=status.HTTP_204_NO_CONTENT
        )

        return Response(status=status.HTTP_204_NO_CONTENT)
