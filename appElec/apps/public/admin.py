from django.contrib import admin
from .models import Logo


class LogoAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "image"]
    readonly_fields = [
        "name",
    ]


# Register your models here.
admin.site.register(Logo, LogoAdmin)
