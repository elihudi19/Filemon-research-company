from django.contrib import admin

from .models import Sector


@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ("name_en", "slug", "is_published", "order")
    prepopulated_fields = {"slug": ("name_en",)}
    list_filter = ("is_published",)
    ordering = ("order",)
