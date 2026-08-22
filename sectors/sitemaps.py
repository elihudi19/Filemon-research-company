from django.contrib.sitemaps import Sitemap

from .models import Sector


class SectorSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.7

    def items(self):
        return Sector.objects.filter(is_published=True)
