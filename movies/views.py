from django.shortcuts import render
from django.http import HttpResponse
from movies.models import Movie, Character
from rest_framework.response import Response # type: ignore
from rest_framework.decorators import api_view, permission_classes# type: ignore
from rest_framework.permissions import IsAuthenticatedOrReadOnly # type: ignore
from .serializers import MovieSerializer, CharacterSerializer
from rest_framework import status  # type: ignore
from rest_framework import generics # type: ignore


class movie_index(generics.ListAPIView):
    queryset=Movie.objects.all()
    serializer_class = MovieSerializer

class movie_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_url_kwarg = "movie_id"

class add_movie(generics.ListCreateAPIView):
    queryset=Movie.objects.all()
    serializer_class = MovieSerializer


class character_index(generics.ListAPIView):
    queryset=Character.objects.all()
    serializer_class = CharacterSerializer

class character_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Character.objects.all()
    serializer_class = CharacterSerializer
    lookup_url_kwarg = "character_id"

class add_character(generics.ListCreateAPIView):
    queryset=Character.objects.all()
    serializer_class = CharacterSerializer

