from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from .models import Logo
import os


# Eliminar imagenes al momento de borrar registro
@receiver(post_delete, sender=Logo)
def delete_image_signal_device(sender, instance, **kargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)


# Eliminar imagenes al momento de actualizar registro
@receiver(pre_save, sender=Logo)
def change_image_signal_device(sender, instance, **kargs):
    if not instance.pk:
        return False

    try:
        old_file = Logo.objects.get(pk=instance.pk).image
    except Logo.DoesNotExist:
        return False

    new_file = instance.image

    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)

        
