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
