from django.urls import path

from . import views

app_name = "proposals"

urlpatterns = [
    path("", views.contact_request, name="contact"),
    path("asante/", views.thank_you, name="thank_you"),
]
