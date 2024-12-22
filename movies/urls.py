from django.urls import path

from . import views

urlpatterns = [
    path("", views.movie_index, name="index"),
    path("characters/", views.character_index),
    path("<int:movie_id>/", views.movie_detail, name="detail"),
    path("characters/<int:character_id>/", views.character_detail),
]
