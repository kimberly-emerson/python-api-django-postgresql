"""
tba
"""

from django.contrib.auth.models import Group
from rest_framework import serializers


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """
    tba
    """

    class Meta:
        """
        tba
        """

        model = Group
        fields = ['url', 'name']
