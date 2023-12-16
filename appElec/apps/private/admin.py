from django.contrib import admin
from .models import MobileToken, Tag, Material, Provider, Budget, MaterialGroup, MaterialMount 


class BudgetAdmin(admin.ModelAdmin):
    list_display = ["id", "code", "owner"]
    list_filter = ["owner", "code"]

admin.site.register(MobileToken)


admin.site.register(Material)
admin.site.register(Tag)
admin.site.register(Provider)

admin.site.register(Budget, BudgetAdmin)
admin.site.register(MaterialGroup)
admin.site.register(MaterialMount)
