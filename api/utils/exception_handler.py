from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status


def custom_exception_handler(exc, context):
    # Call DRF's default exception handler to get the standard error response
    response = exception_handler(exc, context)

    if response is not None:
        # Customize the error response format here
        data = {
            'status_code': response.status_code,
            'error_type': exc.__class__.__name__,
            'message': response.data
        }
        response.data = data
    return response