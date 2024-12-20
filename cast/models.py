from django.db import models
from reviews.models import Review
from django.contrib.contenttypes.fields import GenericRelation
# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField()
    role = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    review = GenericRelation(Review)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
   





