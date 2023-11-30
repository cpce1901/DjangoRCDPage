from django.contrib import admin
from .models import Logo, MobileToken, Tag, Material, Budget, BudgetMaterial, Provider


class BudgetAdmin(admin.ModelAdmin):
    list_display = ["code", "owner", "total_price"]
    list_filter = ["owner", "code"]


class BudgetMaterialAdmin(admin.ModelAdmin):
    list_display = ["code_budget", "name_budget", "material", "quantity", "total_price"]
    list_filter = [
        "budget__owner",
        "budget__code",
    ]

    def code_budget(self, obj):
        return obj.budget.code

    def name_budget(self, obj):
        return obj.budget.owner

    code_budget.short_description = "Presupuesto"
    name_budget.short_description = "Cliente"


# Register your models here.
admin.site.register(Logo)
admin.site.register(MobileToken)


admin.site.register(Material)
admin.site.register(Tag)
admin.site.register(Provider)

admin.site.register(BudgetMaterial, BudgetMaterialAdmin)
admin.site.register(Budget, BudgetAdmin)
