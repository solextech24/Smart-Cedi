"""
Development settings for Smart Cedi project.

This file imports from base.py and adds development-specific configurations.
Use this for local development only - never in production!
"""

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# In development, we allow all hosts for convenience
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']

# Database configuration for development
# We'll start with SQLite for simplicity, then move to PostgreSQL later
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Development-specific apps
DEV_APPS = [
    'django_extensions',  # Provides useful management commands
]

# Add development apps to installed apps
INSTALLED_APPS += DEV_APPS

# Console email backend for development
# Emails will be printed to console instead of actually sent
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Disable CORS restrictions in development
CORS_ALLOW_ALL_ORIGINS = True

# Show detailed error pages in development
DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request: DEBUG,
}