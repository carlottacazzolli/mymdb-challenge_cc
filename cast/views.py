from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
from django.template import loader
# Create your views here.



def index(request):
    people = Person.objects.order_by("-first_name")
    template = loader.get_template("cast/index.html")
    context = {
        "people": people,
    }
    return HttpResponse(template.render(context, request))

def detail(request, person_id):
    person = Person.objects.get(pk=person_id)
    reviews = person.review.all()  # Access reviews via GenericRelation
    return render(request, "cast/detail.html", {"person": person, "reviews":reviews})