from django.shortcuts import render
from reviews.models import Review
from rest_framework import status  # type: ignore
from rest_framework import generics # type: ignore 
from .serializer import ReviewSerializer
# Create your views here.


class index(generics.ListAPIView):
    queryset=Review.objects.all()
    serializer_class = ReviewSerializer

class detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_url_kwarg = "review_id"

class add_review(generics.ListCreateAPIView):
    queryset=Review.objects.all()
    serializer_class = ReviewSerializer