from django.contrib import admin
from .models import Message

# Register your models here.


class AdminMessage(admin.ModelAdmin):
    list_display = ["name", "address", "phone", "email", "details", "created"]
    search_fields = ["name"]
    list_filter = [
        "created",
    ]

admin.site.register(Message, AdminMessage)
