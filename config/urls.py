from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.http import HttpResponse
from django.urls import include, path

from insights.sitemaps import ArticleSitemap, PublicationSitemap
from sectors.sitemaps import SectorSitemap

sitemaps = {
    "sectors": SectorSitemap,
    "publications": PublicationSitemap,
    "articles": ArticleSitemap,
}


def healthz(request):
    """Render inatumia hii kuangalia kama app iko hai."""
    return HttpResponse("ok")


urlpatterns = [
    # Njia ya admin imefichwa — inasomwa kutoka ADMIN_URL_PATH (env var)
    path(settings.ADMIN_URL_PATH, admin.site.urls),

    path("healthz", healthz, name="healthz"),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),

    path("", include("core.urls")),
    path("sekta/", include("sectors.urls")),
    path("huduma/", include("services.urls")),
    path("maktaba/", include("insights.urls")),
    path("mawasiliano/", include("proposals.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Kurasa maalum za makosa (zinatumika DEBUG=False)
handler404 = "core.views.error_404"
handler500 = "core.views.error_500"
