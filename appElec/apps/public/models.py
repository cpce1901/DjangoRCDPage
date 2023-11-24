from django.db import models

# Create your models here.


class Menssage(models.Model):
    name = models.CharField("Nombre", max_length=256)
    email = models.EmailField("Email")
    phone = models.IntegerField("Telefono")
    address = models.CharField("Dirección", max_length=256)
    details = models.TextField("Detalles")
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.details}"
