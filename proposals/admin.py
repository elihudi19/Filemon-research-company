from django.contrib import admin

from .models import ProposalRequest


@admin.register(ProposalRequest)
class ProposalRequestAdmin(admin.ModelAdmin):
    list_display = ("full_name", "organization", "email", "sector", "status", "created_at", "submitted_ip")
    list_filter = ("status", "sector", "created_at")
    search_fields = ("full_name", "organization", "email")
    readonly_fields = ("submitted_ip", "created_at")
    date_hierarchy = "created_at"

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser
