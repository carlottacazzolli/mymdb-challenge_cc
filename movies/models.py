from django.db import models
from cast.models import Person
# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    description = models.CharField()
    director = models.ForeignKey(Person, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"


class Character(models.Model):
    actor = models.ForeignKey(Person, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nickname}"