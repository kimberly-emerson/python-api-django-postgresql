"""
"""

import logging
from typing import Any
from rest_framework import status, filters, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from api.sales.models.sales_territory_model import SalesTerritory
from api.sales.serializers.sales_territory_serializer import (
    SalesTerritorySerializer
)
from api.config.build_swagger_schema import build_schema_extension
from api.utils.logging_handler import log_event


logger = logging.getLogger(__name__)


class SalesTerritoryPagination(viewsets.ModelViewSet):
    """
    # Pagination configuration for SalesTerritory API endpoints.

    # Attributes:
    #     - page_size (int): Default number of items per page (10).
    #     - page_size_query_param (str): Query parameter to override the page
    #     size.
    #     - max_page_size (int): Maximum allowed page size (100).
    # """
    # page_size: int = 10
    # page_size_query_param: str = 'page_size'
    # max_page_size: int = 100


class SalesTerritoryViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing SalesTerritory resources.

    Provides standard CRUD operations along with filtering, ordering,
    authentication, and Swagger schema integration.

    Logging:
        Each method uses `log_event` to record structured JSON logs, including:
          - User performing the action
          - HTTP method and path
          - Resource ID (if applicable)
          - Response status code
    """
    model: str = SalesTerritory.__name__
    basename: str = 'address-types'
    lookup_field: str = 'sales_territory_id'
    # pylint: disable=no-member
    queryset = SalesTerritory.objects.all().order_by(lookup_field)
    serializer_class = SalesTerritorySerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head',
                         'options']

    filter_backends = [filters.OrderingFilter]
    ordering_fields = [f'{lookup_field}']
    ordering = [f'{lookup_field}']

    @build_schema_extension(
        model=model,
        operation_id='list',
        serializer=SalesTerritorySerializer,
        success_code=200,
        tags=['Sales']
    )
    def list(
        self,
        request: Request,
        *args: Any,
        **kwargs: Any
    ) -> Response:
        """
        Retrieve a paginated list of all SalesTerritory resources.

        Args:
            request (Request): The HTTP request instance.

        Returns:
            Response: A JSON response containing the count and serialized data.

        Logging:
            Logs request context and total count of results.
        """
        log_event(
            "INFO",
            "SalesTerritory list requested",
            user=str(request.user),
            method=request.method,
            path=request.get_full_path()
        )

        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = SalesTerritorySerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = SalesTerritorySerializer(queryset, many=True)

        log_event(
            "INFO",
            "SalesTerritory list retrieved",
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
        serializer=SalesTerritorySerializer,
        success_code=200,
        tags=['Sales']
    )
    def retrieve(
        self,
        request: Request,
        *args: Any,
        **kwargs: Any,
    ) -> Response:
        """
        Retrieve a single SalesTerritory resource by ID.

        Args:
            request (Request): The HTTP request instance.

        Returns:
            Response: A JSON response containing the serialized SalesTerritory
            data.

        Logging:
            Logs the ID of the retrieved SalesTerritory and request context.
        """
        instance: SalesTerritory = self.get_object()
        log_event(
            "INFO",
            "SalesTerritory retrieved",
            user=str(request.user),
            id=instance.sales_territory_id,
            method=request.method,
            path=request.get_full_path(),
            status=status.HTTP_200_OK
        )

        serializer = self.get_serializer(instance)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    @build_schema_extension(
        model=model,
        operation_id='create',
        serializer=SalesTerritorySerializer,
        success_code=201,
        tags=['Sales']
    )
    def create(
        self,
        request: Request,
        *args: Any,
        **kwargs: Any,
    ) -> Response:
        """
        Create a new SalesTerritory resource.

        Args:
            request (Request): The HTTP request instance containing request
            data.

        Returns:
            Response: A JSON response containing the serialized newly created
            SalesTerritory.

        Logging:
            Logs payload keys (not sensitive values) and the created
            SalesTerritory ID.
        """
        log_event(
            "INFO",
            "Create SalesTerritory request received",
            user=str(request.user),
            method=request.method,
            path=request.get_full_path(),
            payload_keys=list(request.data.keys())
        )

        serializer: SalesTerritorySerializer = self.get_serializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        instance: SalesTerritory = serializer.save()

        log_event(
            "INFO",
            "SalesTerritory created successfully",
            user=str(request.user),
            id=instance.sales_territory_id,
            status=status.HTTP_201_CREATED
        )

        return Response(
            {'data': serializer.data},
            status=status.HTTP_201_CREATED
        )

    @build_schema_extension(
        model=model,
        operation_id='update',
        serializer=SalesTerritorySerializer,
        success_code=200,
        tags=['Sales']
    )
    def update(
        self,
        request: Request,
        *args: Any,
        **kwargs: Any,
    ) -> Response:
        """
        Update an existing SalesTerritory resource.

        Args:
            request (Request): The HTTP request instance containing updated
            data.

        Returns:
            Response: A JSON response containing the updated serialized
            SalesTerritory.

        Logging:
            Logs the ID being updated, payload keys, and outcome status.
        """
        instance: SalesTerritory = self.get_object()
        log_event(
            "INFO",
            "Update SalesTerritory request received",
            user=str(request.user),
            id=instance.sales_territory_id,
            method=request.method,
            path=request.get_full_path(),
            payload_keys=list(request.data.keys())
        )

        serializer: SalesTerritorySerializer = self.get_serializer(
            instance,
            data=request.data,
            partial=False
        )
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        log_event(
            "INFO",
            "SalesTerritory updated successfully",
            user=str(request.user),
            id=instance.sales_territory_id,
            status=status.HTTP_200_OK
        )

        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    @build_schema_extension(
        model=model,
        operation_id='update',
        serializer=SalesTerritorySerializer,
        success_code=200,
        tags=['Sales']
    )
    def partial_update(
        self,
        request: Request,
        *args: Any,
        **kwargs: Any,
    ) -> Response:
        """
        Partially update an existing SalesTerritory resource.

        Args:
            request (Request): The HTTP request instance containing partial
            data.

        Returns:
            Response: A JSON response containing the updated serialized
            SalesTerritory.

        Logging:
            Logs the ID being patched, payload keys, and outcome status.
        """
        instance: SalesTerritory = self.get_object()
        log_event(
            "INFO",
            "Partial update request for SalesTerritory",
            user=str(request.user),
            id=instance.sales_territory_id,
            method=request.method,
            path=request.get_full_path(),
            payload_keys=list(request.data.keys())
        )

        serializer: SalesTerritorySerializer = self.get_serializer(
            instance,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        log_event(
            "INFO",
            "SalesTerritory partially updated successfully",
            user=str(request.user),
            id=instance.sales_territory_id,
            status=status.HTTP_200_OK
        )

        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    @build_schema_extension(
        model=model,
        operation_id='destroy',
        serializer=SalesTerritorySerializer,
        success_code=204,
        tags=['Sales']
    )
    def destroy(
        self,
        request: Request,
        *args: Any,
        **kwargs: Any,
    ) -> Response:
        """
        Delete an SalesTerritory resource.

        Args:
            request (Request): The HTTP request instance.

        Returns:
            Response: An empty response with 204 No Content status.

        Logging:
            Logs the ID being deleted and the outcome status.
        """
        instance: SalesTerritory = self.get_object()
        log_event(
            "WARNING",
            "Delete SalesTerritory request received",
            user=str(request.user),
            id=instance.sales_territory_id,
            method=request.method,
            path=request.get_full_path()
        )

        instance.delete()

        log_event(
            "INFO",
            "SalesTerritory deleted successfully",
            user=str(request.user),
            id=instance.sales_territory_id,
            status=status.HTTP_204_NO_CONTENT
        )

        return Response(status=status.HTTP_204_NO_CONTENT)
