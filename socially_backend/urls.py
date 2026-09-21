"""
Django URLs configuration for socially_backend project.
"""
from django.contrib import admin
from django.urls import path, include
from apps.core.views import health_check

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', health_check, name='top-level-health-check'),
    path('api/health/', health_check, name='api-health-check'),
    path('api/', include('apps.core.urls')),
]
