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

MQTT_SERVER = "146.190.124.66"
MQTT_PORT = 1883
MQTT_KEEPALIVE = 60
MQTT_USER = "Pc"
MQTT_PASSWORD = "Pc"
MQTT_TOPIC = "rcdPage/notification"


