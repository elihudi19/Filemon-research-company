from django.urls import path

from . import views

app_name = "insights"

urlpatterns = [
    path("ripoti/", views.publication_list, name="publication_list"),
    path("ripoti/<slug:slug>/", views.publication_detail, name="publication_detail"),
    path("makala/", views.article_list, name="article_list"),
    path("makala/<slug:slug>/", views.article_detail, name="article_detail"),
]
