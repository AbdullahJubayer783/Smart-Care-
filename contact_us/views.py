from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ContactUsSerializers
from .models import ContactUs
# Create your views here.

class ContactUsViewsets(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializers

