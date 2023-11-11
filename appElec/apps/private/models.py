from django.db import models

# Create your models here.
class Logo(models.Model):
    name = models.CharField('Logo',max_length=128, unique=True)
    image = models.ImageField(upload_to= 'media/private')

    def __str__(self):
        return f"{self.name}"
    
    