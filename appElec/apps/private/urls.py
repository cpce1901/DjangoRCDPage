from django.urls import path
from .views import (
    MessagesApi,
    MessageDetailApi,
    MessageAddApi,
    MessageUpdateApi,
    MessageDeleteApi,
)

app_name = "private_app"

urlpatterns = [
    path("messages/list/", MessagesApi.as_view(), name="messages"),
    path("messages/detail/<int:pk>", MessageDetailApi.as_view(), name="messages-detail"),
    path("messages/add/", MessageAddApi.as_view(), name="messages-add"),
    path("messages/update/<int:pk>", MessageUpdateApi.as_view(), name="messages-update"),
    path("messages/delete/<int:pk>", MessageDeleteApi.as_view(), name="messages-delete"),
]