"""
Serializers for the custom Group model defined in api.models.user_model.

This module provides a HyperlinkedModelSerializer for exposing group-related
data in RESTful APIs. It enables hyperlinked navigation and selective field
representation for role-based access and contributor grouping.

Exposed fields:
    - url: Hyperlinked reference to the group detail endpoint
    - name: Display name of the group
"""

from django.contrib.auth.models import Group
from rest_framework import serializers


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the custom Group model using hyperlinked relationships.

    This serializer enables RESTful representation of group data, including
    navigable links to group detail views. It is suitable for use in APIs
    that manage contributor roles, permissions, or organizational grouping.

    Attributes:
        Meta (class): Configuration class specifying model and fields.
    """

    class Meta:
        """
        Configuration class for GroupSerializer.

        Specifies the model to serialize and the fields to include in API
        responses.

        This setup ensures consistent exposure of group identifiers and
        navigation links.

        Attributes:
            model (Group): The custom Group model from api.models.user_model.
            fields (list): Fields to include in the serialized output:
                - 'url': Hyperlinked reference to the group detail endpoint
                - 'name': Display name of the group
        """

        model = Group
        fields = ['url', 'name']
