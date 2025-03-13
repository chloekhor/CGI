"""
WSGI config for backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ['HTTPS'] = "on"  #Nigel change on 13/3 to test HTTPS

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

application = get_wsgi_application()


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

application = get_wsgi_application()

if os.environ.get('HTTPS_ENABLED', 'false').lower() == 'true':
    from hypercorn.config import Config
    config = Config()
    config.bind = ["0.0.0.0:8000"]
    config.certfile = "C:/nginx/ssl/localhost.crt"
    config.keyfile = "C:/nginx/ssl/localhost.key"