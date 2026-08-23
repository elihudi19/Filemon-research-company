import logging

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django_ratelimit.decorators import ratelimit
from honeypot.decorators import check_honeypot

from proposals.views import get_client_ip

from .forms import JobApplicationForm
from .models import JobPosting

logger = logging.getLogger("django.security")


def job_list(request):
    jobs = JobPosting.objects.filter(is_published=True)
    return render(request, "careers/job_list.html", {"jobs": jobs})


def job_detail(request, slug):
    job = get_object_or_404(JobPosting, slug=slug, is_published=True)
    return render(request, "careers/job_detail.html", {"job": job})


@check_honeypot
@ratelimit(key="ip", rate="5/h", method="POST", block=False)
def apply(request, slug):
    job = get_object_or_404(JobPosting, slug=slug, is_published=True)
    was_limited = getattr(request, "limited", False)

    if request.method == "POST" and was_limited:
        logger.warning("Rate limit imefikiwa kwa IP %s kwenye maombi ya kazi.", get_client_ip(request))
        messages.error(
            request,
            "Umetuma maombi mengi kwa muda mfupi. Tafadhali subiri kidogo kisha ujaribu tena.",
        )
        return render(request, "careers/apply.html", {"form": JobApplicationForm(), "job": job})

    if request.method == "POST":
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.submitted_ip = get_client_ip(request)
            application.save()

            try:
                send_mail(
                    subject=f"[Ombi la Kazi Mpya] {job.title_en}",
                    message=(
                        f"Nafasi: {job.title_en}\n"
                        f"Jina: {application.full_name}\n"
                        f"Barua pepe: {application.email}\n"
                        f"Simu: {application.phone}\n\n"
                        f"Ujumbe:\n{application.cover_message}"
                    ),
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.PROPOSAL_NOTIFY_EMAIL],
                    fail_silently=True,
                )
            except Exception:
                logger.exception("Imeshindwa kutuma barua pepe ya taarifa ya ombi la kazi.")

            messages.success(request, "Asante! Ombi lako la kazi limepokelewa.")
            return redirect("careers:thank_you")
    else:
        form = JobApplicationForm()

    return render(request, "careers/apply.html", {"form": form, "job": job})


def thank_you(request):
    return render(request, "careers/thank_you.html")
