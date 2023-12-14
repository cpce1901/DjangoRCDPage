from django.db import models
import os


# Create your models here.
class Logo(models.Model):
    def change_name(instance, filename):
        ext = filename.split(".")[-1]
        filename = f"logo.{ext}"
        return os.path.join("private/logo/", filename)

    name = models.CharField("Logo", max_length=128, unique=True, default="logo")
    image = models.ImageField(upload_to=change_name)

    class Meta:
        verbose_name = "Logo"
        verbose_name_plural = "Logos"

    def __str__(self):
        return f"{self.name}"


class MobileToken(models.Model):
    name = models.CharField("Nombre", max_length=255)
    token = models.CharField("Token", max_length=255, unique=True)

    class Meta:
        verbose_name = "Token de telefono"
        verbose_name_plural = "Token de telefonos"

    def __str__(self):
        return f"{self.name} - {self.token}"


class Tag(models.Model):
    name = models.CharField("Nombre", max_length=128)

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"

    def __str__(self):
        return f"{self.name}"


class Provider(models.Model):
    name = models.CharField("Nombre", max_length=128)

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"

    def __str__(self):
        return f"{self.name}"


class Material(models.Model):
    unit_choices = [("0", "gl"), ("1", "c/u"), ("2", "m"), ("3", "tira")]

    description = models.CharField("Descripción", max_length=512)
    unit = models.CharField("unidad", max_length=1, choices=unit_choices)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name="Marca")
    provider = models.ForeignKey(
        Provider, on_delete=models.CASCADE, verbose_name="Proveedor"
    )
    price = models.PositiveIntegerField("Precio")

    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materiales"

    def __str__(self):
        return f"{self.description}"


# Presupuesto = Budget
class Budget(models.Model):
    code = models.CharField("Código", max_length=8, unique=True)
    owner = models.CharField("Cliente", max_length=128)

    class Meta:
        verbose_name = "Presupuesto"
        verbose_name_plural = "Presupuestos"

    def __str__(self):
        return f"Código: {self.code}, Cliente: {self.owner}"


class MaterialMount(models.Model):
    mount = models.PositiveIntegerField("Cantidad")
    material = models.ManyToManyField(Material, verbose_name="Materiales")

    class Meta:
        verbose_name = "Cantidad de material"
        verbose_name_plural = "Cantidad de materiales"

    def __str__(self):
        return f"Cantidad: {self.mount}, Material: {self.material}"


class MaterialGroup(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    materials = models.ManyToManyField(MaterialMount, verbose_name="Materiales")

    class Meta:
        verbose_name = "Grupo de material"
        verbose_name_plural = "Grupo de materiales"

    def __str__(self):
        return f"Código: {self.budget}, Cliente: {self.materials}"
