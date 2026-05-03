from django.urls import path
from . import views

urlpatterns = [
    path("", views.entry, name="entry"),
    path("dashboard/", views.index, name="index"),
]
