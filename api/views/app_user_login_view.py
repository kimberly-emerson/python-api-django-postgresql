"""
API view for user authentication and token generation
Accepts a POST request with `username` and `password`, authenticates the user
using Django's built-in `authenticate()` method, and returns an authentication
token if credentials are valid

This view is designed for login endpoints in token-based authentication flows
using `rest_framework.authtoken`

Returns:
    - 200 OK with `{'token': <auth_token>}` if authentication succeeds
    - 401 Unauthorized with `{'error': 'Invalid credentials'}` if it fail

Example request:
    POST /api/login/
    {
        "username": "kimberly",
        "password": "password123"

Example response:
    {
        "token": "abc123xyz456"
    }
"""

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


class UserLoginView(APIView):
    """
    Handles user authentication and token issuance via POST request.

    This view accepts a username and password, authenticates the user using Django's 
    built-in `authenticate()` method, and returns a token for use in subsequent 
    authenticated API calls. It supports token-based authentication using 
    `rest_framework.authtoken`.

    Intended for login endpoints in RESTful APIs where clients need to obtain 
    a token after successful authentication.

    Attributes:
        None

    Example:
        POST /api/login/
        {
            "username": "kimberly",
            "password": "password123"
        }

    Successful Response:
        HTTP 200 OK
        {
            "token": "abc123xyz456"
        }

    Error Response:
        HTTP 401 Unauthorized
        {
            "error": "Invalid credentials"
        }
    """

    def post(self, request):    
        """
        Authenticates a user and returns an authentication token.

        This method handles POST requests containing `username` and `password`
        fields.

        It uses Django's `authenticate()` to verify credentials and returns a
        token via `rest_framework.authtoken` if authentication is successful.

        Args:
            request (Request): The incoming HTTP request with login credentials
            in `request.data`.

        Returns:
            Response:
                - HTTP 200 OK with `{'token': <auth_token>}` if credentials are
                valid.
                - HTTP 401 Unauthorized with `{'error': 'Invalid credentials'}`
                if authentication fails.

        Example:
            POST /api/login/
            {
                "username": "kimberly",
                "password": "password123"
            }

        Notes:
            - Token is created if it doesn't already exist for the user.
            - Ensure `rest_framework.authtoken` is included in `INSTALLED_APPS`
            and migrations are applied.
        """

        user = authenticate(username=request.data['username'],
                            password=request.data['password'])
        if user:
            token = Token.objects.get_or_create(user=user)  # pylint: disable=no-member
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=401)
