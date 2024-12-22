from codecs import lookup
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Person
from django.template import loader
from rest_framework import status  # type: ignore
from cast.serializers import PersonSerializer
from rest_framework.response import Response # type: ignore
from rest_framework.decorators import api_view, permission_classes# type: ignore
from rest_framework.permissions import IsAuthenticatedOrReadOnly # type: ignore
from rest_framework import generics # type: ignore




class index(generics.ListAPIView):
    queryset=Person.objects.all()
    serializer_class = PersonSerializer

class detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Person.objects.all()
    serializer_class = PersonSerializer
    lookup_url_kwarg = "person_id"

class addPerson(generics.ListCreateAPIView):
    queryset=Person.objects.all()
    serializer_class = PersonSerializer
