from django.db import models
from django.urls import reverse


class Sector(models.Model):
    name_en = models.CharField(max_length=150)
    name_sw = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    summary_en = models.TextField()
    summary_sw = models.TextField()
    icon = models.CharField(max_length=50, default="bar-chart-2")
    is_published = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name_en

    def get_absolute_url(self):
        return reverse("sectors:detail", kwargs={"slug": self.slug})
