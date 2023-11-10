from django.contrib import admin
from django.urls import path
from .views import Home
from django.conf import settings
from django.conf.urls.static import static

app_name = "public_app"

urlpatterns = [
    path("", Home.as_view(), name="home"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
