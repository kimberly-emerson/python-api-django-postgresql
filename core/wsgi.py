"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from decouple import config

match config('APP_ENV'):
    case "dev":
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dev")
    case "test":
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test")

application = get_wsgi_application()
