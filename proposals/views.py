import logging

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django_ratelimit.decorators import ratelimit
from honeypot.decorators import check_honeypot

from .forms import ProposalRequestForm

logger = logging.getLogger("django.security")


def get_client_ip(request):
    """Inasoma IP halisi ya mtumiaji hata nyuma ya proxy ya Render."""
    xff = request.META.get("HTTP_X_FORWARDED_FOR")
    if xff:
        return xff.split(",")[0].strip()
    return request.META.get("REMOTE_ADDR")


@check_honeypot
@ratelimit(key="ip", rate="5/h", method="POST", block=False)
def contact_request(request):
    was_limited = getattr(request, "limited", False)

    if request.method == "POST" and was_limited:
        logger.warning("Rate limit imefikiwa kwa IP %s kwenye fomu ya RFP.", get_client_ip(request))
        messages.error(
            request,
            "Umetuma maombi mengi kwa muda mfupi. Tafadhali subiri kidogo kisha ujaribu tena.",
        )
        return render(request, "proposals/contact.html", {"form": ProposalRequestForm()})

    if request.method == "POST":
        form = ProposalRequestForm(request.POST, request.FILES)
        if form.is_valid():
            proposal = form.save(commit=False)
            proposal.submitted_ip = get_client_ip(request)
            proposal.save()

            try:
                send_mail(
                    subject=f"[RFP Mpya] {proposal.organization}",
                    message=(
                        f"Jina: {proposal.full_name}\n"
                        f"Taasisi: {proposal.organization}\n"
                        f"Barua pepe: {proposal.email}\n"
                        f"Simu: {proposal.phone}\n\n"
                        f"Ujumbe:\n{proposal.message}"
                    ),
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.PROPOSAL_NOTIFY_EMAIL],
                    fail_silently=True,
                )
            except Exception:
                logger.exception("Imeshindwa kutuma barua pepe ya taarifa ya RFP.")

            messages.success(
                request,
                "Asante! Ombi lako limepokelewa. Timu yetu itawasiliana nawe hivi karibuni.",
            )
            return redirect("proposals:thank_you")
    else:
        form = ProposalRequestForm()

    return render(request, "proposals/contact.html", {"form": form})


def thank_you(request):
    return render(request, "proposals/thank_you.html")
