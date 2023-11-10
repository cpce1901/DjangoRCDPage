from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from django.conf import settings
from django.conf.urls.static import static
from .sitemap import StaticViewSitemap
from .views import robots_txt

sitemaps = {
    "static": StaticViewSitemap,
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.public.urls")),
    # Bots.txt
    path("robots.txt", robots_txt),
    # Sitemaps
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Vistas Errores
handler404 = "appElec.views.error_404_view"

# Nombre Admin
admin.site.site_title = "Panel de control Electricidad RCD spa"
admin.site.site_header = "Electricidad RCD spa"
admin.site.index_title = "Panel de control Electricidad RCD spa"
