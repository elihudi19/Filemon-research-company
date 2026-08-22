from django.contrib.sitemaps import Sitemap

from .models import Article, Publication


class PublicationSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return Publication.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.published_date


class ArticleSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        return Article.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.published_date
