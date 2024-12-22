from django.urls import path, include

from . import views


urlpatterns = [
    path("", views.index.as_view()),
    path("<int:review_id>/", views.detail.as_view()),
    path("add/", views.add_review.as_view())
]