from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import ShowSerializer
from .models import Show

class ShowList(generics.ListCreateAPIView):
    queryset = Show.objects.all().order_by('id') 
    serializer_class = ShowSerializer 

class ShowDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Show.objects.all().order_by('id')
    serializer_class = ShowSerializer
