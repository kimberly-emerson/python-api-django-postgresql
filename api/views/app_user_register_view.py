"""
API view for user registration.

This view handles POST requests to create new `AppUser` instances using the
`AppUserSerializer`. It is publicly accessible and does not require
authentication, making it suitable for onboarding workflows and open
registration endpoints.

Features:
- Accepts `username`, `email`, and `password` fields
- Uses `AppUserSerializer` for validation and data handling
- Allows unauthenticated access via `permissions.AllowAny`

Example request:
    POST /api/register/
    {
        "username": "kimberly",
        "email": "kimberly@example.com",
        "password": "password123"
    }

Successful response:
    HTTP 201 Created
    {
        "username": "kimberly",
        "email": "kimberly@example.com"
    }


Notes:
    - Ensure `AUTH_USER_MODEL = 'api.models.AppUser'` is set in `settings.py`
    - Extend `AppUserSerializer` to hash passwords or include additional fields
"""


from rest_framework import generics, permissions
from api.schemas.app_user_serializer import AppUserSerializer


class UserRegistrationView(generics.CreateAPIView):
    """
    API view for user registration.

    This view handles POST requests to create new `AppUser` instances using the
    `AppUserSerializer`. It is publicly accessible and does not require
    authentication, making it suitable for onboarding workflows and open
    registration endpoints.

    Features:
    - Accepts `username`, `email`, and `password` fields
    - Uses `AppUserSerializer` for validation and data handling
    - Allows unauthenticated access via `permissions.AllowAny`

    Example request:
        POST /api/register/
        {
            "username": "kimberly",
            "email": "kimberly@example.com",
            "password": "password123"
        }

    Successful response:
        HTTP 201 Created
        {
            "username": "kimberly",
            "email": "kimberly@example.com"
        }

    Notes:
        - Ensure `AUTH_USER_MODEL = 'api.models.AppUser'` is set in
        `settings.py`
        - Extend `AppUserSerializer` to hash passwords or include additional
        fields.
    """
    serializer_class = AppUserSerializer
    permission_classes = [permissions.AllowAny]
