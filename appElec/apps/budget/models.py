from django.db import models


# Create your models here.
class Tag(models.Model):
    name = models.CharField("Nombre", max_length=128)

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"


class Provider(models.Model):
    name = models.CharField("Nombre", max_length=128)

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"


class Client(models.Model):
    name = models.CharField("Nombre", max_length=256)

    def __str__(self):
        return self.name


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


class MaterialMount(models.Model):
    mount = models.PositiveIntegerField("Cantidad")
    material = models.ForeignKey(Material, verbose_name="Materiales", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Cantidad de material"
        verbose_name_plural = "Cantidad de materiales"

    def subtotal(self):
        return self.mount * self.material.price

    def __str__(self):
        return f"Cantidad: {self.mount}, Material: {self.material.description}"


# Presupuesto = Budget
class Budget(models.Model):
    code = models.CharField("Código", max_length=8, unique=True)
    owner = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Cliente")
    items = models.ManyToManyField(MaterialMount, verbose_name="Items", blank=True)

    class Meta:
        verbose_name = "Presupuesto"
        verbose_name_plural = "Presupuestos"

    def total(self):
        return sum(item.subtotal() for item in self.items.all())


    def __str__(self):
        return f"Código: {self.code}, Cliente: {self.owner}"
