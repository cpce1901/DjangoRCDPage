from django.contrib import sitemaps
from django.urls import reverse
import datetime

class StaticViewSitemap(sitemaps.Sitemap):
    lastmod = datetime.datetime.now().date()
    priority = 0.8
    changefreq = "daily"
    protocol = 'https'

    def items(self):
        return ["public_app:home"]
    
    def location(self, item):
        return reverse(item)