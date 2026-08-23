from django.db import models
from django.urls import reverse

from core.validators import validate_document_file


class Publication(models.Model):
    """Research Reports & Whitepapers - zinazoweza kupakuliwa (PDF)."""
    title_en = models.CharField(max_length=200)
    title_sw = models.CharField(max_length=200)
    summary_en = models.TextField()
    summary_sw = models.TextField()
    cover_image = models.ImageField(upload_to="articles/", blank=True, null=True)
    video_url = models.URLField(
        blank=True,
        help_text="Bandika link ya YouTube au Vimeo (hiari). Mfano: https://www.youtube.com/watch?v=XXXXXXXXXXX",
    )
    document = models.FileField(
        upload_to="publications/files/",
        validators=[validate_document_file],
        help_text="PDF pekee, upeo wa 5MB.",
    )
    published_date = models.DateField()
    is_published = models.BooleanField(default=True)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ["-published_date"]

    def __str__(self):
        return self.title_en

    def get_absolute_url(self):
        return reverse("insights:publication_detail", kwargs={"slug": self.slug})


class Article(models.Model):
    """Blog & Articles - uchambuzi wa mwelekeo wa masoko na takwimu."""
    title_en = models.CharField(max_length=200)
    title_sw = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    body_en = models.TextField()
    body_sw = models.TextField()
    cover_image = models.ImageField(upload_to="articles/", blank=True, null=True)
    author_name = models.CharField(max_length=150)
    published_date = models.DateField()
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ["-published_date"]

    def __str__(self):
        return self.title_en

    def get_absolute_url(self):
        return reverse("insights:article_detail", kwargs={"slug": self.slug})
