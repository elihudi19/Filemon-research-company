from django.db import models
from django.urls import reverse


class Service(models.Model):
    title_en = models.CharField(max_length=150)
    title_sw = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True)
    description_en = models.TextField()
    description_sw = models.TextField()
    icon = models.CharField(max_length=50, default="clipboard")
    order = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title_en

    def get_absolute_url(self):
        return reverse("services:detail", kwargs={"slug": self.slug})
