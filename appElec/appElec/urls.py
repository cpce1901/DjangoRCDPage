from django.contrib import admin
from django.urls import path, include, register_converter
from django.contrib.sitemaps.views import sitemap
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .sitemap import StaticViewSitemap
from .views import robots_txt, error_404_view
from .converter import FloatUrlParameterConverter

register_converter(FloatUrlParameterConverter, "float")

schema_view = get_schema_view(
    openapi.Info(
        title="Documentation API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=False,
    permission_classes=(permissions.IsAdminUser,),
)

sitemaps = {
    "static": StaticViewSitemap,
}

urlpatterns = [
    # Site
    path("admin/", admin.site.urls),
    path("", include("apps.public.urls")),
    path("", include("apps.contact.urls")),
    # Bots.txt
    path("robots.txt", robots_txt),
    # Sitemaps
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    # Documentacion API
    path(
        "swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    # routes
    path("", include("apps.budget.routers")),
    path("", include("apps.materials.routers")),
    path("", include("apps.contact.routers")),
    path("", include("apps.utills.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Vistas Errores
handler404 = error_404_view

# Nombre Admin
admin.site.site_title = "Panel de control Electricidad RCD spa"
admin.site.site_header = "Electricidad RCD spa"
admin.site.index_title = "Panel de control Electricidad RCD spa"
