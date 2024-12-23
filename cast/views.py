from tempfile import template
from django.shortcuts import render, redirect
from .models import Person
from cast.serializers import PersonSerializer
from rest_framework.response import Response # type: ignore
from rest_framework import generics # type: ignore
from rest_framework.renderers import TemplateHTMLRenderer  # type: ignore
from django.urls import reverse



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
 
    
   