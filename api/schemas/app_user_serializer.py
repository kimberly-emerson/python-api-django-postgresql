"""
🔐 Serializer for user registration and profile creation

Maps the `AppUser` model fields to JSON-compatible representations for
API input/output. Includes write-only handling for passwords to ensure
they are never exposed in API responses

Features:
- Serializes `username`, `email`, and `password` fields
- Ensures `password` is write-only for security
- Ready for use in registration views, onboarding flows, or user creation
endpoint

Extend this serializer to:
- Add custom validation (e.g., password strength, email domain checks)
- Hash passwords before saving
- Include additional profile fields (e.g., `bio`, `role`, `profile_image`

Example usage:
    serializer = AppUserSerializer(data=request.data)
    if serializer.is_valid():
        user = AppUser.objects.create_user(**serializer.validated_data)
"""

from rest_framework import serializers
from api.models.app_user_model import AppUser


class AppUserSerializer(serializers.ModelSerializer):
    """
    🔐 Serializer for creating and managing AppUser instances.

    This serializer maps essential fields from the `AppUser` model for use in
    registration, onboarding, and authentication workflows. It ensures that
    the `password` field is write-only, preventing it from being exposed in
    API responses.

    Features:
    - Serializes `username`, `email`, and `password`
    - Ensures password confidentiality via `write_only=True`
    - Ready for use in user creation views or onboarding endpoints

    Extend this serializer to:
    - Add custom validation (e.g. password strength, email format)
    - Hash passwords before saving
    - Include additional profile fields (e.g. `bio`, `role`, `avatar`)

    Example:
        serializer = AppUserSerializer(data=request.data)
        if serializer.is_valid():
            AppUser.objects.create_user(**serializer.validated_data)
    """
    password = serializers.CharField(write_only=True)

    class Meta:
        """
        Configuration class for AppUserSerializer.

        Specifies the model and fields to be included in serialization. This
        setup ensures that only the `username`, `email`, and `password` fields
        from the `AppUser` model are exposed through the API.

        Attributes:
            model (Model): The Django model to serialize (`AppUser`).
            fields (tuple): A tuple of field names to include in the serialized
            output.
        """
        model = AppUser
        fields = ('username', 'email', 'password')
