from os import read
from rest_framework import serializers # type: ignore
from .models import Person
from reviews.models import Review
from reviews.serializer import ReviewSerializer

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    review = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Person
        fields = ("id","first_name", "last_name", "birthday", "role", "review")
        
