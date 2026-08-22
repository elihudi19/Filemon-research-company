from django.conf import settings


def company_context(request):
    return {
        "COMPANY_NAME": settings.COMPANY_NAME,
        "COMPANY_SHORT_NAME": settings.COMPANY_SHORT_NAME,
    }
