from rest_framework import serializers # type: ignore
from .models import Movie, Character
from cast.serializers import PersonSerializer
from reviews.serializer import ReviewSerializer

class MovieSerializer(serializers.ModelSerializer):
    director = PersonSerializer(read_only=True)
    review = ReviewSerializer(many=True)
    class Meta():
        model= Movie
        fields = ('id', 'title', 'release_date', 'description', 'director', 'review')


class CharacterSerializer(serializers.ModelSerializer):
    actor = PersonSerializer()
    movie = MovieSerializer()
    review = ReviewSerializer(many=True)
    class Meta():
        model= Character
        fields = ('id', 'nickname', 'movie', 'actor', 'review')