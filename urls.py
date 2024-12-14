
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger setup
schema_view = get_schema_view(
   openapi.Info(
      title="ALX Travel App API",
      default_version='v1',
      description="API documentation for the ALX Travel App",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@alxtravelapp.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-docs'),
    path('api/', include('listings.urls')),  # Include your app URLs
]
