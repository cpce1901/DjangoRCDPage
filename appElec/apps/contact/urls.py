from django.urls import path
from .views import Contact

app_name = "contact_app"

urlpatterns = [
    path("contacto/", Contact.as_view(), name="contact"),
]
