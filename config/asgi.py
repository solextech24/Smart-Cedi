"""
ASGI config for Smart Cedi project.

ASGI (Asynchronous Server Gateway Interface) enables Django to handle 
WebSockets, background tasks, and other async features.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

# Set the default settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')

application = get_asgi_application()