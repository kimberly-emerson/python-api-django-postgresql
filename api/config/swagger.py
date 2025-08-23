"""
Swagger/OpenAPI Schema Configuration for Django REST Framework

This module sets up the auto-generated API documentation using `drf_yasg`,
providing a public Swagger UI and schema endpoint for the Django project.

Components:
- `schema_view`: Configured via `get_schema_view()` to expose OpenAPI metadata
  including title, version, description, contact, and license. Accessible via
  URL routing (e.g., `/swagger/` or `/redoc/`).
- `TaggedAutoSchema`: Custom schema inspector that overrides tag generation
  logic. If a view defines `swagger_tags`, they are used; otherwise, it falls
  back to default tag inference.

Usage:
- Include `schema_view.with_ui('swagger')` or `schema_view.with_ui('redoc')`
  in your `urls.py` to expose interactive documentation.
- Extend `TaggedAutoSchema` in your views or viewsets to customize tag behavior
  for grouped documentation.

Dependencies:
- Django REST Framework
- drf_yasg
"""

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from drf_yasg.inspectors import SwaggerAutoSchema
from rest_framework import permissions

from api.schemas.api_error_serializer import ApiErrorSerializer


schema_view = get_schema_view(  # pylint: disable=invalid-name
   openapi.Info(
      title="Python API",
      default_version='v1',
      description="Python API (Django, Django REST Framework, PostgreSQL) "
                  "managed by PDM",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="kimberly.emerson@outlook.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

error_responses = {
  400: openapi.Response(description="BAD REQUEST: The server couldn't"
                        "understand the request due to invalid syntax or"
                        "missing parameters.",
                        schema=ApiErrorSerializer,
                        examples={
                                    'application/json': {
                                          "type": "validation_error",
                                          "errors": [
                                              {
                                                  "code": "required",
                                                  "detail": "This field is"
                                                            "required.",
                                                  "attr": "name"
                                              }
                                          ]
                                     }
                                  }),
  401: openapi.Response(description="UNAUTHORIZED: Authentication is required"
                        "and has either failed or not been provided.",
                        schema=ApiErrorSerializer,
                        examples={
                            'application/json': {
                                "type": "client_error",
                                "errors": [
                                    {
                                        "code": "not_authenticated",
                                        "detail": "Authentication credentials"
                                                  "were not provided.",
                                        "attr": "null"
                                    }
                                ]
                            }
                        }),
  403: openapi.Response(description="FORBIDDEN: The server understood the"
                        "request but refuses to authorize it.",
                        schema=ApiErrorSerializer,
                        examples={
                            'application/json': {
                                  "type": "client_error",
                                  "errors": [
                                      {
                                          "code": "permission_denied",
                                          "detail": "You do not have"
                                                    "permission to perform"
                                                    "this action.",
                                          "attr": "null"
                                      }
                                  ]
                            }
                        }),
  404: openapi.Response(description="NOT FOUND: The requested resource could"
                        "not be found on the server.",
                        schema=ApiErrorSerializer,
                        examples={
                            'application/json': {
                                  "type": "client_error",
                                  "errors": [
                                      {
                                          "code": "not_found",
                                          "detail": "Not found.",
                                          "attr": "null"
                                      }
                                  ]
                              }
                        }),
  405: openapi.Response(description="METHOD NOT ALLOWED: The HTTP method used"
                        "is not supported for the requested resource.",
                        schema=ApiErrorSerializer,
                        examples={
                            'application/json': {
                                  "type": "client_error",
                                  "errors": [
                                      {
                                          "code": "method_not_allowed",
                                          "detail": "Method \"POST\" not"
                                                    "allowed.",
                                          "attr": 'null'
                                      }
                                  ]
                              }
                        }),
  406: openapi.Response(description="NOT ACCEPTABLE: The requested resource is"
                        "not capable of generating content acceptable to the"
                        "client.",
                        schema=ApiErrorSerializer,
                        examples={
                            'application/json': {
                                  "type": "client_error",
                                  "errors": [
                                      {
                                          "code": "not_acceptable",
                                          "detail": "",
                                          "attr": 'null'
                                      }
                                  ]
                              }
                        }),
  415: openapi.Response(description="UNSUPPORTED MEDIA TYPE: The server"
                        "refuses to accept the request because the payload"
                        "format is unsupported.",
                        schema=ApiErrorSerializer,
                        examples={
                            'application/json': {
                                  "type": "client_error",
                                  "errors": [
                                      {
                                          "code": "method_not_allowed",
                                          "detail": "Method \"POST\" not"
                                                    "allowed.",
                                          "attr": 'null'
                                      }
                                  ]
                              }
                        }),
  429: openapi.Response(description="TOO MANY REQUESTS: The user has sent too"
                        "many requests in a given amount of time (rate"
                        "limiting).",
                        schema=ApiErrorSerializer,
                        examples={
                            'application/json': {
                                  "type": "client_error",
                                  "errors": [
                                      {
                                          "code": "too_many_requests",
                                          "detail": "Method \"POST\" not"
                                                    "allowed.",
                                          "attr": 'null'
                                      }
                                  ]
                              }
                        }),
  500: openapi.Response(description="INTERNAL SERVER ERROR: A generic error"
                        "occurred on the server; often indicates an unhandled"
                        "exception.",
                        schema=ApiErrorSerializer,
                        examples={
                            'application/json': {
                                  "type": "server_error",
                                  "errors": [
                                      {
                                          "code": "internal_server_error",
                                          "detail": "",
                                          "attr": 'null'
                                      }
                                  ]
                              }
                        }),
}


class TaggedAutoSchema(SwaggerAutoSchema):
    """
    Custom Swagger schema class for dynamic tag assignment in DRF views.

    This subclass of `SwaggerAutoSchema` overrides the default tag generation
    behavior used by `drf_yasg`. It enables views or viewsets to explicitly
    define their Swagger tags via a `swagger_tags` attribute.

    If `self.view.swagger_tags` is present, those tags are used in the
    generated OpenAPI documentation. Otherwise, it falls back to the default
    tag inference based on operation keys.

    Example:
        class MyViewSet(viewsets.ModelViewSet):
            swagger_tags = ['Analytics']

    Args:
        operation_keys (list, optional): Keys used to infer default tags if
        `swagger_tags` is not defined.

    Returns:
        list: A list of tags to be applied to the Swagger operation.
    """
    def get_tags(self, operation_keys=None):
        return getattr(self.view, 'swagger_tags', super()
                       .get_tags(operation_keys))
