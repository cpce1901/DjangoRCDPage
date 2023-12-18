from django.contrib import admin
from django.utils.html import format_html
from .models import Budgets, Items, Clients, BudgetItems


class BudgetItemsInline(admin.TabularInline):
    model = BudgetItems
    extra = 1  # Cuántos formularios de items mostrar por defecto


class ItemsAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "mount",
        "unit_material",
        "material_name",
        "subtotal",
        "material_owner",
        "material_ppto"
    ]

    def unit_material(self, obj):
        return obj.material.get_unit_display()

    def material_name(self, obj):
        return obj.material.description

    def material_owner(self, obj):
        return (
            obj.budgetitems_set.first().budget.owner.name
            if obj.budgetitems_set.exists()
            else ""
        )
    
    def material_ppto(self, obj):
        return (
            obj.budgetitems_set.first().budget.code
            if obj.budgetitems_set.exists()
            else ""
        )

    unit_material.short_description = "Unidad"
    material_name.short_description = "Descripción"
    material_owner.short_description = "Propietario"
    material_ppto.short_description = "Presupuesto"


class BudgetsAdmin(admin.ModelAdmin):
    list_display = ["id", "code", "owner", "materials_list", "total"]
    list_filter = ["owner", "code"]
    inlines = [BudgetItemsInline]

    def materials_list(self, obj):
        materials = obj.items.all()
        print(obj)
        material_list = [
            f"<li>{ material.mount} {material.material.get_unit_display()} {material.material.description}</li>"
            for material in materials
        ]

        if material_list:
            materials_html = "<ul>" + "".join(material_list) + "</ul>"
            return format_html(materials_html)
        else:
            return "No existen materiales en este PPTO... "

    materials_list.short_description = "Lista de materiales"


admin.site.register(Clients)
admin.site.register(Items, ItemsAdmin)
admin.site.register(Budgets, BudgetsAdmin)
