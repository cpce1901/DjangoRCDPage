from django.db import models

# Create your models here.


class Message(models.Model):
    name = models.CharField("Nombre", max_length=256)
    email = models.EmailField("Email")
    phone = models.CharField("Telefono", max_length=13)
    address = models.CharField("Dirección", max_length=256)
    details = models.TextField("Detalles")
    readed = models.BooleanField("Leido", default=False)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.details}"
    
class MobileToken(models.Model):
    name = models.CharField("Nombre", max_length=255)
    token = models.CharField("Token", max_length=255, unique=True)

    class Meta:
        verbose_name = "Token de telefono"
        verbose_name_plural = "Token de telefonos"

    def __str__(self):
        return f"{self.name} - {self.token}"
