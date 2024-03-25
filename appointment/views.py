from django.shortcuts import render
from rest_framework import viewsets
from . import models 
from . import serialalizers
# Create your views here.

class AppointmentViewset(viewsets.ModelViewSet):
    queryset = models.Appointment.objects.all()
    serializer_class = serialalizers.AppointmentSerializers

    def get_queryset(self):
        queryset = super().get_queryset()
        patient_id = self.request.query_params.get('patient_id')
        print(patient_id)
        if patient_id:
            queryset = queryset.filter(patient_id=patient_id)
        return queryset
