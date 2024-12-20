from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.core.exceptions import ValidationError
from sympy import content
# from cast.models import Person
# from movies.models import Movie, Character



# Create your models here.

class Review(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to={
        "model__in": ["movie", "person", "character"]  
    })
    object_id = models.IntegerField() #TODO: find a better way to do this
    content_object = GenericForeignKey('content_type', 'object_id')
    review_text = models.TextField()
    rating = models.IntegerField()  # e.g., 1-5 stars
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
      return f"Review for {self.content_object} ({self.rating}/5)"
  
    # def clean(self):
        
    #     if self.content_type.model == 'person':
    #         try:
    #             Person.objects.get(id=self.object_id)
    #         except Person.DoesNotExist:
    #             raise ValidationError(f"No person found with id {self.object_id}")
    #     elif self.content_type.model == 'movie':
    #         try:
    #             Movie.objects.get(id=self.object_id)
    #         except Movie.DoesNotExist:
    #             raise ValidationError(f"No movie found with id {self.object_id}")
    #     elif self.content_type.model == 'character':
    #         try:
    #             Character.objects.get(id=self.object_id)
    #         except Character.DoesNotExist:
    #             raise ValidationError(f"No character found with id {self.object_id}")
    #     super().clean()


# class Review(models.Model):
#     review_text = models.TextField(default=None)
#     rating = models.IntegerField(default=None)  # e.g., 1-5 stars
#     content = GenericRelation(Review_gfk)


#     def __str__(self):
#         return f"Review for {content} ({self.rating}/5)"
