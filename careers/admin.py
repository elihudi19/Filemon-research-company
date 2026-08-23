from django.contrib import admin

from .models import JobApplication, JobPosting


@admin.register(JobPosting)
class JobPostingAdmin(admin.ModelAdmin):
    list_display = ("title_en", "employment_type", "location", "is_published", "posted_date")
    list_filter = ("is_published", "employment_type")
    prepopulated_fields = {"slug": ("title_en",)}
    date_hierarchy = "posted_date"


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ("full_name", "job", "email", "status", "created_at")
    list_filter = ("status", "job")
    search_fields = ("full_name", "email")
    readonly_fields = ("submitted_ip", "created_at")
    date_hierarchy = "created_at"

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser
