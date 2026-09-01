from django.conf import settings
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.http import HttpResponse
from django.urls import include, path, re_path
from django.views.static import serve

from insights.sitemaps import ArticleSitemap, PublicationSitemap
from sectors.sitemaps import SectorSitemap
from careers.sitemaps import JobPostingSitemap

sitemaps = {
    "sectors": SectorSitemap,
    "publications": PublicationSitemap,
    "articles": ArticleSitemap,
    "jobs": JobPostingSitemap,
}


def healthz(request):
    return HttpResponse("ok")


urlpatterns = [
    path(settings.ADMIN_URL_PATH, admin.site.urls),
    path("healthz", healthz, name="healthz"),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    path("", include("core.urls")),
    path("sekta/", include("sectors.urls")),
    path("huduma/", include("services.urls")),
    path("maktaba/", include("insights.urls")),
    path("mawasiliano/", include("proposals.urls")),
    path("ajira/", include("careers.urls")),
]

# Kuonyesha faili za /media/ (picha, CV, ToR) — KILA WAKATI, siyo DEBUG pekee.
# Django's static() helper ya kawaida INAZUIA kufanya kazi endapo DEBUG=False
# (hata ukiiita ndani ya 'if' yako mwenyewe), kwa hiyo tunatumia moja kwa
# moja 'django.views.static.serve' ambayo haina ukomo huo. Hii ni "wavu wa
# usalama" endapo Cloudinary bado haijawekwa, au kwa faili za awali
# zilizohifadhiwa kwenye disk ya ndani ya server.
urlpatterns += [
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
]

handler404 = "core.views.error_404"
handler500 = "core.views.error_500"
