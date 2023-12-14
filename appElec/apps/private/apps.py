from django.apps import AppConfig


class PrivateConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.private"

    def ready(self):
        from . import signals
