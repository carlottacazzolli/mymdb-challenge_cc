from django.urls import path, include

from . import views


urlpatterns = [
    # path("", views.index, name="person_index"),
    path("", views.index),
    path("<int:person_id>/", views.detail, name="person_detail"),
]