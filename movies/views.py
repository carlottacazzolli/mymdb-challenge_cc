from django.shortcuts import render
from django.http import HttpResponse
from movies.models import Movie, Character

# Create your views here.

def index(request):
    movies = Movie.objects.order_by("-title")
    return render(request, "movies/index.html", {"movies": movies})


def detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    characters = Character.objects.filter(movie=movie)
    return render(request, "movies/detail.html", {"movie": movie, 'characters':characters})