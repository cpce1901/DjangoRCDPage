from django.contrib import admin
from .models import Tag, Material, Provider, Budget, MaterialGroup, MaterialMount 
from import_export.resources import ModelResource
from import_export.admin import ExportActionModelAdmin, ImportExportModelAdmin

class MaterialResource(ModelResource):

    class Meta:
        model = Material
        use_bulk = True
        batch_size = 500
        

class MaterialAdmin(ImportExportModelAdmin, ExportActionModelAdmin):
    resource_class = MaterialResource
    list_display = ["id", "tag", "unit", "description", "price", "provider"]
    search_fields = ["description",]
    list_filter = ["provider", "tag",]

class BudgetAdmin(admin.ModelAdmin):
    list_display = ["id", "code", "owner"]
    list_filter = ["owner", "code"]




admin.site.register(Material, MaterialAdmin)
admin.site.register(Tag)
admin.site.register(Provider)

admin.site.register(Budget, BudgetAdmin)
admin.site.register(MaterialGroup)
admin.site.register(MaterialMount)
