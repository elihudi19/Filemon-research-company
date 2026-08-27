from django.shortcuts import render

from insights.models import Publication
from sectors.models import Sector
from services.models import Service

from .models import ClientTestimonial, CoreValue, ImpactStat, TeamMember


def home(request):
    context = {
        "sectors": Sector.objects.filter(is_published=True)[:5],
        "services": Service.objects.filter(is_published=True)[:6],
        "stats": ImpactStat.objects.all(),
        "publications": Publication.objects.filter(is_published=True)[:3],
        "testimonials": ClientTestimonial.objects.filter(is_published=True)[:6],
    }
    return render(request, "core/home.html", context)


def about(request):
    context = {
        "core_values": CoreValue.objects.all(),
        "team": TeamMember.objects.filter(is_leadership=True),
    }
    return render(request, "core/about.html", context)


def methodology(request):
    return render(request, "core/methodology.html")


def compliance(request):
    return render(request, "core/compliance.html")


def error_404(request, exception=None):
    return render(request, "errors/404.html", status=404)


def error_500(request):
    return render(request, "errors/500.html", status=500)
