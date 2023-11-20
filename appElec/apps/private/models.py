from django.db import models
import os


# Create your models here.
class Logo(models.Model):
    def change_name(instance, filename):
        ext = filename.split(".")[-1]
        filename = f"logo.{ext}"
        return os.path.join("media/private", filename)

    name = models.CharField("Logo", max_length=128, unique=True)
    image = models.ImageField(upload_to=change_name)

    def __str__(self):
        return f"{self.name}"


