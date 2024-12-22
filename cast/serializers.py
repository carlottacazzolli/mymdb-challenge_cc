from rest_framework import serializers # type: ignore
from .models import Person
from reviews.serializer import ReviewSerializer

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    review = ReviewSerializer(many=True)

    class Meta:
        model = Person
        fields = ("id","first_name", "last_name", "birthday", "role", "review")
        