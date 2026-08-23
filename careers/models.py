from django.db import models
from django.urls import reverse

from core.validators import validate_document_file


class JobPosting(models.Model):
    EMPLOYMENT_TYPE_CHOICES = [
        ("full_time", "Full-Time"),
        ("part_time", "Part-Time"),
        ("contract", "Contract"),
        ("internship", "Internship"),
    ]

    title_en = models.CharField(max_length=200)
    title_sw = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    department_en = models.CharField(max_length=150, blank=True)
    department_sw = models.CharField(max_length=150, blank=True)
    employment_type = models.CharField(max_length=20, choices=EMPLOYMENT_TYPE_CHOICES, default="part_time")
    location = models.CharField(max_length=150, default="Dar es Salaam, Tanzania")
    description_en = models.TextField()
    description_sw = models.TextField()
    requirements_en = models.TextField(blank=True)
    requirements_sw = models.TextField(blank=True)
    application_deadline = models.DateField(null=True, blank=True)
    is_published = models.BooleanField(default=True)
    posted_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["-posted_date"]

    def __str__(self):
        return self.title_en

    def get_absolute_url(self):
        return reverse("careers:job_detail", kwargs={"slug": self.slug})


class JobApplication(models.Model):
    STATUS_CHOICES = [
        ("new", "Mpya"),
        ("reviewing", "Inapitiwa"),
        ("shortlisted", "Amechaguliwa Awali"),
        ("rejected", "Hakufaulu"),
        ("hired", "Ameajiriwa"),
    ]

    job = models.ForeignKey(JobPosting, on_delete=models.CASCADE, related_name="applications")
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    cover_message = models.TextField()
    resume = models.FileField(
        upload_to="careers/resumes/",
        validators=[validate_document_file],
        help_text="CV/Resume (PDF/DOC), upeo wa 5MB.",
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="new")

    submitted_ip = models.GenericIPAddressField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.full_name} - {self.job.title_en} ({self.created_at:%Y-%m-%d})"
