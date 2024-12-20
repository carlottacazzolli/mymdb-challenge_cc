from django.contrib import admin
from movies.models import Movie, Character

# Register your models here.

class MovieChoice(admin.ModelAdmin):
    list_display = ["id", "title"]

class CharacterChoice(admin.ModelAdmin):
    list_display = ["id", "nickname"]

admin.site.register(Movie, MovieChoice)
admin.site.register(Character, CharacterChoice)
