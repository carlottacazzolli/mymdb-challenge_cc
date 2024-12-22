from rest_framework import serializers # type: ignore
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta():
        model= Review
        fields = ('id', 'review_text', 'rating')
