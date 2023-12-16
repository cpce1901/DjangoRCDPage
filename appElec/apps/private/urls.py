from django.urls import path
from .views import (
    MobileTokenApiView,
    MobileTokenDetail,
)

app_name = "private_app"

urlpatterns = [

    path("mobile-token/", MobileTokenApiView.as_view(), name="mobile-token"),
    path("mobile-token/<int:pk>/", MobileTokenDetail.as_view(), name="mobile-token-detail"),

]
