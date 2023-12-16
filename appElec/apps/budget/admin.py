from django.contrib import admin
from django.utils.html import format_html
from import_export.resources import ModelResource
from import_export.admin import ExportActionModelAdmin, ImportExportModelAdmin
from .models import Tags, Materials, Providers, Budgets, Items, Clients, BudgetItems


class BudgetItemsInline(admin.TabularInline):
    model = BudgetItems
    extra = 1  # Cuántos formularios de items mostrar por defecto

class MaterialsResource(ModelResource):
    class Meta:
        model = Materials
        use_bulk = True
        batch_size = 500


class MaterialsAdmin(ImportExportModelAdmin, ExportActionModelAdmin):
    resource_class = MaterialsResource
    list_display = ["id", "tag", "unit", "description", "price", "provider"]
    search_fields = [
        "description",
    ]
    list_filter = [
        "provider",
        "tag",
    ]



class ItemsAdmin(admin.ModelAdmin):
    list_display = ["id", "mount", "subtotal"]

    def show_budget(self, obj):
        return obj.items.owner
    

class BudgetsAdmin(admin.ModelAdmin):
    list_display = ["id", "code", "owner","materials_list", "total" ]
    list_filter = ["owner", "code"]
    inlines = [BudgetItemsInline]
   

    def materials_list(self, obj):
        materials = obj.items.all()
        material_list = [f"<li>{ material.mount} {material.material.get_unit_display()} {material.material.description}</li>" for material in materials]

        if material_list:
            materials_html = "<ul>" + "".join(material_list) + "</ul>"
            return format_html(materials_html)
        else:
            return "No existen materiales en este PPTO... "

    materials_list.short_description = "Lista de materiales"


admin.site.register(Materials, MaterialsAdmin)
admin.site.register(Tags)
admin.site.register(Providers)


admin.site.register(Clients)
admin.site.register(Items, ItemsAdmin)
admin.site.register(Budgets, BudgetsAdmin)
