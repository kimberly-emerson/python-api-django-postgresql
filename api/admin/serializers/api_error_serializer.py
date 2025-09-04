"""
tba
"""
from rest_framework import serializers
from api.admin.models.api_error_model import ApiError

class ApiErrorSerializer(serializers.ModelSerializer):
    """
    Serializer for API error objects.

    Standardizes error response structure for Swagger and real API errors.
    """

    class Meta:
        """
        tba
        """
        model = ApiError
        fields = [
            "id", "code", "detail", "attr", "error_type",
            "path", "method", "user", "created_at"
        ]
