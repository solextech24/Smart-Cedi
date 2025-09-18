"""
WSGI config for Smart Cedi project.

WSGI (Web Server Gateway Interface) is the standard for deploying Django apps.
This file is used by WSGI-compatible web servers to serve your project.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Set the default settings module
# In production, this should point to production settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')

application = get_wsgi_application()