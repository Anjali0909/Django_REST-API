from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from .models import Contact
from .serializers import ProjectSerializer


class ListProject(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ProjectSerializer


class DetailProject(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ProjectSerializer
