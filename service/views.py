from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ServiceSerializers
from .models import Service
# Create your views here.

class ServiceViewsets(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializers