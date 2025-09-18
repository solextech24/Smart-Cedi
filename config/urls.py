"""
URL configuration for Smart Cedi project.

This is the main URL router that directs requests to the appropriate views.
We'll organize URLs by feature/app for better maintainability.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Main URL patterns
urlpatterns = [
    # Django admin interface
    path('admin/', admin.site.urls),
    
    # API endpoints will go here
    # path('api/v1/', include('api.urls')),
    
    # Frontend pages will go here
    # path('', include('frontend.urls')),
]

# Serve media files in development
# In production, this should be handled by the web server (nginx, apache, etc.)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)