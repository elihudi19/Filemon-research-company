from django.conf import settings


def company_context(request):
    lang = getattr(request, "LANG", "en")
    tagline = settings.COMPANY_FULL_NAME_EN if lang == "en" else settings.COMPANY_FULL_NAME_SW
    return {
        "COMPANY_NAME": settings.COMPANY_NAME,
        "COMPANY_SHORT_NAME": settings.COMPANY_SHORT_NAME,
        "COMPANY_TAGLINE": tagline,
        "LANG": lang,
    }
