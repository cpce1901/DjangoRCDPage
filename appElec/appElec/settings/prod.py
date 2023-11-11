from .base import *

DEBUG = True

ALLOWED_HOSTS = ['167.172.170.1', '*']

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "elecrcdprod",  # Nombre DB
        "USER": "cpce1901",  # Nombre usuario
        "PASSWORD": "cpce1901",  # Password
        "HOST": "localhost",
        "PORT": "3306",
        "OPTIONS": {
            "sql_mode": "STRICT_TRANS_TABLES",
        },
    }
}


STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static/'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media/'