from django.contrib import admin

from .models import Article, Publication


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ("title_en", "published_date", "is_published")
    list_filter = ("is_published",)
    prepopulated_fields = {"slug": ("title_en",)}
    date_hierarchy = "published_date"


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title_en", "author_name", "published_date", "is_published")
    list_filter = ("is_published",)
    prepopulated_fields = {"slug": ("title_en",)}
    date_hierarchy = "published_date"
