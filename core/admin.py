from django.contrib import admin

from .models import ClientTestimonial, CoreValue, ImpactStat, TeamMember


@admin.register(ImpactStat)
class ImpactStatAdmin(admin.ModelAdmin):
    list_display = ("number", "label_en", "order")
    ordering = ("order",)


@admin.register(CoreValue)
class CoreValueAdmin(admin.ModelAdmin):
    list_display = ("title_en", "order")
    ordering = ("order",)


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("full_name", "role_en", "is_leadership", "order")
    list_filter = ("is_leadership",)
    ordering = ("order",)


@admin.register(ClientTestimonial)
class ClientTestimonialAdmin(admin.ModelAdmin):
    list_display = ("client_name", "client_organization", "is_published", "order")
    list_filter = ("is_published",)
    ordering = ("order",)
