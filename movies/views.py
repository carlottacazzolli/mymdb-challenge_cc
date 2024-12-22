from django.shortcuts import render
from django.http import HttpResponse
from movies.models import Movie, Character
from rest_framework.response import Response # type: ignore
from rest_framework.decorators import api_view, permission_classes# type: ignore
from rest_framework.permissions import IsAuthenticatedOrReadOnly # type: ignore
from .serializers import MovieSerializer, CharacterSerializer

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def movie_index(request):
    # movies = Movie.objects.order_by("-title")
    # return render(request, "movies/index.html", {"movies": movies})
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def movie_detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    movie_serializer = MovieSerializer(movie)
    return Response(movie_serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def character_index(request):
    characters = Character.objects.all()
    serializer = CharacterSerializer(characters, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def character_detail(request, character_id):
    character = Character.objects.get(pk=character_id)
    serializer = CharacterSerializer(character)
    return Response(serializer.data)