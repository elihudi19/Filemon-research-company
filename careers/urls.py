from django.urls import path

from . import views

app_name = "careers"

urlpatterns = [
    path("", views.job_list, name="job_list"),
    path("<slug:slug>/", views.job_detail, name="job_detail"),
    path("<slug:slug>/omba/", views.apply, name="apply"),
    path("asante/", views.thank_you, name="thank_you"),
]
