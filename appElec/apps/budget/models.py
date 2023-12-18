from django.db import models
from apps.materials.models import Materials


class Clients(models.Model):
    name = models.CharField("Nombre", max_length=256)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.name



class Items(models.Model):
    mount = models.PositiveIntegerField("Cantidad")
    material = models.ForeignKey(
        Materials, verbose_name="Materiales", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"

    def subtotal(self):
        return self.mount * self.material.price

    def __str__(self):
        return f"Cantidad: {self.mount}, Material: {self.material.description}"


class BudgetItems(models.Model):
    budget = models.ForeignKey("Budgets", on_delete=models.CASCADE)
    item = models.ForeignKey("Items", on_delete=models.CASCADE)

    class Meta:
        unique_together = ("budget", "item")

# Presupuesto = Budget
class Budgets(models.Model):
    code = models.CharField("Código", max_length=8, unique=True)
    owner = models.ForeignKey(Clients, on_delete=models.CASCADE, verbose_name="Cliente")
    items = models.ManyToManyField(Items, through=BudgetItems,verbose_name="Items", blank=True)

    class Meta:
        verbose_name = "Presupuesto"
        verbose_name_plural = "Presupuestos"

    def total(self):
        return sum(item.subtotal() for item in self.items.all())

    def __str__(self):
        return f"Código: {self.code}, Cliente: {self.owner}"
