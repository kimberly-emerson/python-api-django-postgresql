"""
tba
"""
import logging
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from api.admin.models.api_error_model import ApiError
from api.admin.serializers.api_error_serializer import ApiErrorSerializer
from api.config.swagger import swagger_for

logger = logging.getLogger(__name__)


class ApiErrorViewSet(viewsets.ModelViewSet):
    """
    ViewSet to manage API error logs.

    Restricted to admin users. Provides read-only access by default,
    but supports CRUD in case admins want to purge or adjust records.
    """
    # pylint: disable=no-member
    queryset = ApiError.objects.all()
    serializer_class = ApiErrorSerializer
    permission_classes = [IsAdminUser]
    lookup_field = "id"
    swagger_tags = ["Errors"]

    @swagger_for("list", ApiErrorSerializer)
    def list(self, request, *args, **kwargs):
        """List all API errors with pagination."""
        return super().list(request, *args, **kwargs)

    @swagger_for("retrieve", ApiErrorSerializer)
    def retrieve(self, request, *args, **kwargs):
        """Retrieve a single API error by ID."""
        return super().retrieve(request, *args, **kwargs)

    @swagger_for("create", ApiErrorSerializer)
    def create(self, request, *args, **kwargs):
        """Manually create an API error entry (for testing/log injection)."""
        logger.warning("[API ERROR] Admin manually creating error: %s",
                       request.data)
        return super().create(request, *args, **kwargs)

    @swagger_for("update", ApiErrorSerializer)
    def update(self, request, *args, **kwargs):
        """Update an API error record."""
        return super().update(request, *args, **kwargs)

    @swagger_for("partial_update", ApiErrorSerializer)
    def partial_update(self, request, *args, **kwargs):
        """Partially update an API error record."""
        return super().partial_update(request, *args, **kwargs)

    @swagger_for("destroy", ApiErrorSerializer)
    def destroy(self, request, *args, **kwargs):
        """Delete an API error record (usually to purge logs)."""
        return super().destroy(request, *args, **kwargs)
