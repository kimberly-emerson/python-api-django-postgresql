"""
Defines a serializer for Django's built-in User model using DRF.

This module exposes selected user fields for API responses and input
validation. It uses HyperlinkedModelSerializer to include URL references
to related resources, supporting RESTful navigation and documentation.

Fields included:
    - url: Hyperlinked reference to the user detail endpoint
    - username: Unique identifier for login and display
    - email: User's email address
    - groups: Related user groups for role-based access control
"""

from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for Django's built-in User model using hyperlinked
    relationships.

    This serializer includes key identity and access fields, and is designed
    for use in RESTful APIs where hyperlinking improves discoverability and
    navigation between resources.

    Attributes:
        Meta.model (User): The Django User model being serialized.
        Meta.fields (list): Specifies the fields to include in the serialized
        output:
            - 'url': Hyperlinked reference to the user detail view
            - 'username': User's unique identifier
            - 'email': Contact email
            - 'groups': Associated user groups for access control
    """

    class Meta:
        """
        Configuration class for the UserSerializer.

        Specifies the model to be serialized and the fields to expose in API
        responses.

        This setup enables hyperlinked navigation and selective field
        inclusion for user-related endpoints.

        Attributes:
            model (User): The Django User model used for serialization.
            fields (list): List of fields to include in the serialized output:
                - 'url': Hyperlinked reference to the user detail view
                - 'username': Unique login/display identifier
                - 'email': User's email address
                - 'groups': Related user groups for role-based access control
        """
        model = User
        fields = ['url', 'username', 'email', 'groups']
