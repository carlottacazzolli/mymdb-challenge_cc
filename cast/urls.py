from django.urls import path, include

from . import views


urlpatterns = [
    # path("", views.index, name="person_index"),
    path("", views.index.as_view(), name="cast_index"),
    path("<int:person_id>/", views.detail.as_view(), name="cast_detail"),
    path("add/", views.addPerson.as_view(), name="add"),
]