from django.contrib import admin
from cast.models import Person
# Register your models here.

class PersonChoice(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name"]

admin.site.register(Person, PersonChoice)
