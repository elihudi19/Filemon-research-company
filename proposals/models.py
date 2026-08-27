from django.db import models

from core.validators import validate_document_file
from sectors.models import Sector


class ProposalRequest(models.Model):
    """Request for Proposal (RFP) - fomu ya mteja anayeomba huduma ya utafiti."""

    STATUS_CHOICES = [
        ("new", "Mpya"),
        ("reviewing", "Inapitiwa"),
        ("contacted", "Mteja Amewasiliana Naye"),
        ("closed", "Imefungwa"),
    ]

    full_name = models.CharField(max_length=150)
    organization = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    sector = models.ForeignKey(Sector, on_delete=models.SET_NULL, null=True, blank=True)
    message = models.TextField()
    tor_document = models.FileField(
        upload_to="proposals/tor/",
        blank=True,
        null=True,
        validators=[validate_document_file],
        help_text="Terms of Reference (PDF/DOC), si lazima. Upeo wa 5MB.",
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="new")

    # Metadata ya usalama / ukaguzi (audit trail)
    submitted_ip = models.GenericIPAddressField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.full_name} - {self.organization} ({self.created_at:%Y-%m-%d})"
