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
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "media/"
MEDIA_DIRS = [BASE_DIR / "media/"]

RECAPTCHA_SITE_KEY = "6LfIbyIpAAAAADeni1j4akCYYGVJ18SAyOJghHUK"
RECAPTCHA_SECRET_KEY = "6LfIbyIpAAAAAPoKadzsZxJagLCfb_mBi0n2d31S"
SILENCED_SYSTEM_CHECKS = ['django_recaptcha.recaptcha_test_key_error']

RECAPTCHA_ERROR_MSG = {
    "required": "Porfavor completa la verificación...",
}
