"""
tba
"""
from decouple import config
from .base import *  # pylint: disable=wildcard-import, unused-wildcard-import


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USERNAME'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOSTNAME'),
        'PORT': config('DB_PORT'),
        "OPTIONS": {
            "options": "-c search_path=admin,people,production,sales,public"
        },
        'ATOMIC_REQUESTS': False,
        'AUTOCOMMIT': True,
        'CONN_MAX_AGE': 0,
        'CONN_HEALTH_CHECKS': False,
        'TIME_ZONE': None,
        'TEST': {
          'CHARSET': None,
          'COLLATION': None,
          'MIGRATE': True,
          'MIRROR': None,
          'NAME': None
        }
    }
}


def get_db_url():
    """
    tba
    """
    return (
        f"postgresql://{DATABASES['USER']}:{DATABASES['PASSWORD']}"
        f"@{DATABASES['HOST']}:{DATABASES['PORT']}/{DATABASES['NAME']}"
    )
