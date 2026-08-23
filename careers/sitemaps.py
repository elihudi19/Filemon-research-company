from django.contrib.sitemaps import Sitemap

from .models import JobPosting


class JobPostingSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return JobPosting.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.posted_date
