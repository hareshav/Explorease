from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from rest_framework import generics
from .models import cab,Hotels,lodge,places
from .serializers import apicab,apilodge,apiHotels,apiplaces
class viewcab(generics.ListCreateAPIView):
    queryset=cab.objects.all()
    serializer_class=apicab
class viewplace(generics.ListCreateAPIView):
    queryset=places.objects.all()
    serializer_class=apiplaces
class viewhotel(generics.ListCreateAPIView):
    queryset=Hotels.objects.all()
    serializer_class=apiHotels
class viewlodge(generics.ListCreateAPIView):
    queryset=lodge.objects.all()
    serializer_class=apilodge