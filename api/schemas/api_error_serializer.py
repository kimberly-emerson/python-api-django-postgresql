"""
"""

from rest_framework import serializers
from api.models.api_error_model import ApiError


class ApiErrorSerializer(serializers.ModelSerializer):
    """
    tba
    """

    class Meta:
        """
        tba
        """
        model = ApiError
        fields = ['description', 'schema', 'example']
