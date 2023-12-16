from django.db import models
import os


# Create your models here.
class Logo(models.Model):
    def change_name(instance, filename):
        ext = filename.split(".")[-1]
        filename = f"logo.{ext}"
        return os.path.join("public/logo/", filename)

    name = models.CharField("Logo", max_length=128, unique=True, default="logo")
    image = models.ImageField(upload_to=change_name)

    class Meta:
        verbose_name = "Logo"
        verbose_name_plural = "Logos"

    def __str__(self):
        return f"{self.name}"
