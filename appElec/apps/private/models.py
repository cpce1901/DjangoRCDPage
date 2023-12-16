from django.db import models


class MobileToken(models.Model):
    name = models.CharField("Nombre", max_length=255)
    token = models.CharField("Token", max_length=255, unique=True)

    class Meta:
        verbose_name = "Token de telefono"
        verbose_name_plural = "Token de telefonos"

    def __str__(self):
        return f"{self.name} - {self.token}"


