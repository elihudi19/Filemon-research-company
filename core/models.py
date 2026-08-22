from django.core.validators import FileExtensionValidator
from django.db import models


class ImpactStat(models.Model):
    """Takwimu za mfano: '100+ Projects Completed'."""
    number = models.CharField(max_length=20, help_text="Mfano: 100+, 50+, 15+")
    label_en = models.CharField(max_length=100)
    label_sw = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.number} {self.label_en}"


class CoreValue(models.Model):
    title_en = models.CharField(max_length=100)
    title_sw = models.CharField(max_length=100)
    description_en = models.TextField()
    description_sw = models.TextField()
    icon = models.CharField(max_length=50, default="shield-check", help_text="Jina la Bootstrap/Feather icon")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title_en


class TeamMember(models.Model):
    full_name = models.CharField(max_length=150)
    role_en = models.CharField(max_length=150)
    role_sw = models.CharField(max_length=150)
    bio_en = models.TextField(blank=True)
    bio_sw = models.TextField(blank=True)
    photo = models.ImageField(
        upload_to="team/",
        blank=True,
        null=True,
        validators=[FileExtensionValidator(["jpg", "jpeg", "png", "webp"])],
    )
    linkedin_url = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_leadership = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.full_name


class ClientTestimonial(models.Model):
    client_name = models.CharField(max_length=150)
    client_organization = models.CharField(max_length=150)
    quote_en = models.TextField()
    quote_sw = models.TextField()
    logo = models.ImageField(
        upload_to="clients/",
        blank=True,
        null=True,
        validators=[FileExtensionValidator(["jpg", "jpeg", "png", "webp", "svg"])],
    )
    is_published = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.client_name} ({self.client_organization})"
