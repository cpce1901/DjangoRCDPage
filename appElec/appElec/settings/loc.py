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

RECAPTCHA_SITE_KEY = "6LdQWSIpAAAAAKueLnjWX_x66ZgvOkTFcSpCKcYM"
RECAPTCHA_SECRET_KEY = "6LdQWSIpAAAAAMwHfTiAGhZXohDP7YwJYI-wzBDA"


RECAPTCHA_ERROR_MSG = {
    "required": "Porfavor completa la verificación...",
}
