from django.db import models
import os


# Create your models here.
class Logo(models.Model):
    
    def change_name(instance, filename):
        ext = filename.split('.')[-1]
        filename = f"logo.{ext}"
        return os.path.join('media/private', filename)

    name = models.CharField("Logo", max_length=128, unique=True)
    image = models.ImageField(upload_to=change_name)

    def __str__(self):
        return f"{self.name}"


class Material(models.Model):
    code = models.PositiveIntegerField("Codigo", unique=True)
    description = models.CharField("Descripcion", max_length=1024)
    unit = models.CharField("Unidad", max_length=8)
    price = models.PositiveIntegerField("Precio")

    def __str__(self):
        return f"{self.code} - {self.description} - {self.unit} - {self.price}"
