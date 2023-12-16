from .base import *

DEBUG = False

ALLOWED_HOSTS = ['167.172.170.1', 'electricidadrcd.cl', 'www.electricidadrcd.cl']

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

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    )
}


STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media/'

RECAPTCHA_PUBLIC_KEY = "6LeQAy0pAAAAADrKe9cNNLEo_r4G6Ppv2OtbVCBU"
RECAPTCHA_PRIVATE_KEY = "6LeQAy0pAAAAAHP4TdTmWuaCwuUmQ_ClrPdoJnyN"

RECAPTCHA_ERROR_MSG = {
    "required": "Porfavor completa la verificación...",
}