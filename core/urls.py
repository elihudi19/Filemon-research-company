from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("kuhusu-sisi/", views.about, name="about"),
    path("mbinu-za-utafiti/", views.methodology, name="methodology"),
    path("uzingatiaji-wa-maadili/", views.compliance, name="compliance"),
]
