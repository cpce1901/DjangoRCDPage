from django.contrib import admin
from import_export.resources import ModelResource
from import_export.admin import ExportActionModelAdmin, ImportExportModelAdmin
from .models import Materials, Providers, Tags


class MaterialsResource(ModelResource):
    class Meta:
        model = Materials
        use_bulk = True
        batch_size = 500


class MaterialsAdmin(ImportExportModelAdmin, ExportActionModelAdmin):
    resource_class = MaterialsResource
    list_display = ["id", "tag", "unit", "description", "price", "provider"]
    ordering=["-id",]
    list_filter = ["provider__name", "tag__name"]
    search_fields = [
        "description",
    ]
    


admin.site.register(Materials, MaterialsAdmin)
admin.site.register(Tags)
admin.site.register(Providers)
