from rest_framework import serializers # type: ignore
from .models import Movie, Character
from cast.models import Person
from cast.serializers import PersonSerializer
from reviews.serializer import ReviewSerializer

class MovieSerializer(serializers.ModelSerializer):
    director = serializers.PrimaryKeyRelatedField(queryset=Person.objects.all())
    review = ReviewSerializer(many=True, read_only=True)
    class Meta():
        model= Movie
        fields = ('id', 'title', 'release_date', 'description', 'director', 'review')


class CharacterSerializer(serializers.ModelSerializer):
    actor = serializers.PrimaryKeyRelatedField(queryset=Person.objects.all())
    movie = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all())
    review = ReviewSerializer(many=True, read_only=True)
    class Meta():
        model= Character
        fields = ('id', 'nickname', 'movie', 'actor', 'review')