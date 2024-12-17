from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:person_id>/", views.detail, name="detail"),
]