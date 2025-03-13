"""
ASGI config for backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

application = get_asgi_application()


if os.environ.get('HTTPS_ENABLED', 'false').lower() == 'true':
    from hypercorn.config import Config
    config = Config()
    config.bind = ["0.0.0.0:8000"]
    config.certfile = "C:/nginx/ssl/localhost.crt"
    config.keyfile = "C:/nginx/ssl/localhost.key"