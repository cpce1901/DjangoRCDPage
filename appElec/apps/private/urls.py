from django.urls import path
from .views import MessagesView, MobileTokenView

app_name = "private_app"

urlpatterns = [
    path("mobile-token/", MobileTokenView.as_view(), name="mobile-token"),
    path("mobile-token/<int:pk>/", MobileTokenView.as_view(), name="mobile-token-detail"),
    path("messages/", MessagesView.as_view(), name="messages"),
    path("messages/<int:pk>/", MessagesView.as_view(), name="messages-detail"),
]
