from django.urls import path
from .views import Contact, MessagesApiView, MessagesDetail

app_name = "contact_app"

urlpatterns = [
    path("contacto/", Contact.as_view(), name="contact"),
    path("messages/", MessagesApiView.as_view(), name="messages"),
    path("messages/<int:pk>/", MessagesDetail.as_view(), name="messages-unit")
]
