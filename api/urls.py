"""
tba
"""

from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)
from api.config.swagger import schema_view
from api.router import router

urlpatterns = [
     path("", include(router.urls)),
     path("api/auth/token",
          TokenObtainPairView.as_view(), name="token_obtain_pair"),
     path("api/auth/token/refresh",
          TokenRefreshView.as_view(), name="token_refresh"),
     path("<format>",
          schema_view.without_ui(cache_timeout=0), name="schema-json"
          ),
     path("api/docs",
          schema_view.with_ui("swagger", cache_timeout=0),
          name="schema-swagger-ui",
          ),
     path("api/docs/redoc",
          schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
     # api project domains
     path('api/people', include('api.people.urls')),
     path('api/production', include('api.production.urls')),
     path('api/sales', include('api.sales.urls')),
]
