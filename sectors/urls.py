from django.urls import path

from . import views

app_name = "sectors"

urlpatterns = [
    path("", views.sector_list, name="list"),
    path("<slug:slug>/", views.sector_detail, name="detail"),
]
