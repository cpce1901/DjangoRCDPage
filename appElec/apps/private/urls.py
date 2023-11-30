from django.urls import path
from .views import (
    MessagesApiView,
    MessagesDetail,
    MobileTokenApiView,
    MobileTokenDetail,
)

app_name = "private_app"

urlpatterns = [
    path("mobile-token/", MobileTokenApiView.as_view(), name="mobile-token"),
    path("mobile-token/<int:pk>/", MobileTokenDetail.as_view(), name="mobile-token-unit"),
    path("messages/", MessagesApiView.as_view(), name="messages"),
    path("messages/<int:pk>/", MessagesDetail.as_view(), name="messages-unit"),
]
