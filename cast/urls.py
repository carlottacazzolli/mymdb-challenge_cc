from django.urls import path, include

from . import views


urlpatterns = [
    # path("", views.index, name="person_index"),
    path("", views.index.as_view()),
    path("<int:person_id>/", views.detail.as_view()),
    path("add/", views.addPerson.as_view()),
]