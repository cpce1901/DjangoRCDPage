from django.contrib import admin
from .models import Message, MobileToken

# Register your models here.


class AdminMessage(admin.ModelAdmin):
    list_display = ["name", "address", "phone", "email", "details", "readed", "created"]
    search_fields = ["name"]
    list_filter = [
        "readed",
        "created",
    ]


class AdminMobileToken(admin.ModelAdmin):
    list_display = ["id", "name", "token"]


admin.site.register(Message, AdminMessage)
admin.site.register(MobileToken, AdminMobileToken)
