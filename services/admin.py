from django.contrib import admin

from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title_en", "is_published", "order")
    list_filter = ("is_published",)
    prepopulated_fields = {"slug": ("title_en",)}
    ordering = ("order",)
