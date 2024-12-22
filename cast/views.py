from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Person
from django.template import loader
from cast.serializers import PersonSerializer
from rest_framework.response import Response # type: ignore
from rest_framework.decorators import api_view, permission_classes# type: ignore
from rest_framework.permissions import IsAuthenticatedOrReadOnly # type: ignore



@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def index(request):
    people = Person.objects.all()
    serializer = PersonSerializer(people, many=True)
    # template = loader.get_template("cast/index.html")
    # context = {
    #     "people": people,
    # }
    # return HttpResponse(template.render(context, request))

    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def detail(request, person_id):
    person = Person.objects.get(pk=person_id)
    reviews = person.review.all()  # Access reviews via GenericRelation
    # return render(request, "cast/detail.html", {"person": person, "reviews":reviews})
    serializer = PersonSerializer(person)
    return Response(serializer.data)