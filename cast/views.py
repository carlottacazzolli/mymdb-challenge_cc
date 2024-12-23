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
    template_name = 'cast/index.html'
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        people = self.queryset.all()
        return Response({'people':people})


class detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Person.objects.all()
    serializer_class = PersonSerializer
    lookup_url_kwarg = "person_id"
    template_name = 'cast/detail.html'
    renderer_classes = [TemplateHTMLRenderer]
    
    def get_object(self):
        person_id = self.kwargs.get(self.lookup_url_kwarg)
        return self.queryset.get(id=person_id)

    def get(self, request, *args, **kwargs):
        person = self.get_object()
        serializer = self.serializer_class(person)
        return Response({'serializer': serializer, 'person': person})
    
    def post(self, request, *args, **kwargs):
        if 'update' in request.POST:

            person = self.get_object()
            serializer = self.serializer_class(person, data=request.data)
            if not serializer.is_valid():
                return Response({'serializer': serializer, 'person': person})
            serializer.save()
            return redirect(reverse('cast_detail', kwargs={'person_id': self.kwargs.get(self.lookup_url_kwarg)}))
        
        else:
            return self.delete(request, *args, **kwargs)
        
    def delete(self, request, *args, **kwargs):

            person = self.get_object()
            person.delete()
            return redirect(reverse('cast_index'))
        
class addPerson(generics.ListCreateAPIView):
    queryset=Person.objects.all()
    serializer_class = PersonSerializer
    template_name = 'cast/add.html'
    renderer_classes = [TemplateHTMLRenderer]
    
    def get(self, request, *args, **kwargs):
        people = self.queryset.all()
        return Response({'people':people})
    
    def perform_create(self, serializer):
        # This method handles saving a new person to the database
        serializer.save()