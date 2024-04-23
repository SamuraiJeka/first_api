from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_views = get_schema_view(
    openapi.Info(
        title="Fake Sneakers",
        default_version="v1"
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)

urlpatterns=[
    re_path('swagger(?P<format>\.json|\.yaml)', schema_views.without_ui(cache_timeout=0), name='schema_json'),
    path('swagger/', schema_views.with_ui('swagger', cache_timeout=0,), name='schema-swagger-ui'),
    path('redoc/', schema_views.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]