from django.urls import path

from . import views

urlpatterns = [
    path("", views.movie_index.as_view(), name="index"),
    path("characters/", views.character_index.as_view()),
    path("<int:movie_id>/", views.movie_detail.as_view(), name="detail"),
    path("characters/<int:character_id>/", views.character_detail.as_view()),
    path("add/", views.add_movie.as_view()),
    path("characters/add/", views.add_character.as_view()),
]
