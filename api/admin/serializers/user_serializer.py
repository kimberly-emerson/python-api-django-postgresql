"""
tba
"""

from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    tba
    """

    class Meta:
        """
        tba
        """
        model = User
        fields = ['url', 'username', 'email', 'groups']
