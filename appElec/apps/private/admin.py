from django.contrib import admin
from .models import Logo, MobileToken, Tag, Material, Provider, Budget, MaterialGroup, MaterialMount 


class BudgetAdmin(admin.ModelAdmin):
    list_display = ["id", "code", "owner"]
    list_filter = ["owner", "code"]

class LogoAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "image"]
    readonly_fields = ["name",]
    


# Register your models here.
admin.site.register(Logo, LogoAdmin)
admin.site.register(MobileToken)


admin.site.register(Material)
admin.site.register(Tag)
admin.site.register(Provider)

admin.site.register(Budget, BudgetAdmin)
admin.site.register(MaterialGroup)
admin.site.register(MaterialMount)
