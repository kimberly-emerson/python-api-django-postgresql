"""
Defines URL patterns for API routing, authentication, and documentation.

Includes endpoints for address type management, JWT token handling, and
interactive API docs using Swagger and ReDoc. Routes are grouped under
the `/api` namespace and secured via token-based authentication.

Endpoints:
    - /api/                  : CRUD routes from registered viewsets
    - /api/auth/             : DRF browseable API login/logout
    - /api/token/            : JWT token obtain endpoint
    - /api/token/refresh/    : JWT token refresh endpoint
    - /api/docs              : Swagger UI documentation
    - /api/docs/redoc        : ReDoc documentation
    - /<format>/             : Raw schema in JSON or YAML format
"""

from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)
from api.config.swagger import schema_view
from api.router import router


urlpatterns = [
    path("", include(router.urls)),
    path("api/auth/", include("rest_framework.urls")),
    path("api/token/",
         TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/",
         TokenRefreshView.as_view(), name="token_refresh"),
    path("<format>/",
         schema_view.without_ui(cache_timeout=0), name="schema-json"
         ),
    path("api/docs",
         schema_view.with_ui("swagger", cache_timeout=0),
         name="schema-swagger-ui",
         ),
    path("api/docs/redoc",
         schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
