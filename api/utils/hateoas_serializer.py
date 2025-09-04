"""
tba
"""
from rest_framework import serializers


class HATEOASLinkSerializer(serializers.Serializer):
    """
    tba
    """
    href = serializers.CharField()
    rel = serializers.CharField()
    method = serializers.CharField()
