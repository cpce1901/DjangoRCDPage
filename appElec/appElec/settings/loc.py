from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "elecrcddev",  # Nombre DB
        "USER": "root",  # Nombre usuario
        "PASSWORD": "cpce1901",  # Password
        "HOST": "localhost",
        "PORT": "3306",
        "OPTIONS": {
            "sql_mode": "STRICT_TRANS_TABLES",
        },
    }
}

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static/"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media_local/"

RECAPTCHA_PUBLIC_KEY = "6LeQAy0pAAAAADrKe9cNNLEo_r4G6Ppv2OtbVCBU"
RECAPTCHA_PRIVATE_KEY = "6LeQAy0pAAAAAHP4TdTmWuaCwuUmQ_ClrPdoJnyN"


RECAPTCHA_ERROR_MSG = {
    "required": "Porfavor completa la verificación...",
}


SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'basic': {
            'type': 'basic'
        }
    },
  
}