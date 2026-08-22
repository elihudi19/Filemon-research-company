from django.shortcuts import get_object_or_404, render

from .models import Sector


def sector_list(request):
    sectors = Sector.objects.filter(is_published=True)
    return render(request, "sectors/list.html", {"sectors": sectors})


def sector_detail(request, slug):
    sector = get_object_or_404(Sector, slug=slug, is_published=True)
    return render(request, "sectors/detail.html", {"sector": sector})
