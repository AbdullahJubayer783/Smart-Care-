from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from rest_framework import filters , pagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly 
from . import models
# Create your views here.

class DoctorPagination(pagination.PageNumberPagination):
    page_size = 2
    page_size_query_param = page_size
    max_page_size = 100

class DoctorViewset(viewsets.ModelViewSet):
    queryset = models.Doctor.objects.all()
    filter_backends = [filters.SearchFilter]
    pagination_class = DoctorPagination
    serializer_class = serializers.DoctorSerializers
    search_fields = ['user__first_name','user__last_name','designation__name','specialization__name',]

class DesignationViewset(viewsets.ModelViewSet):
    queryset = models.Designation.objects.all()
    serializer_class = serializers.DesignationSerializers

class AvailableTimeForSpacificeDoctor(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        doctor_id = request.query_params.get('doctor_id')
        if doctor_id:
            return queryset.filter(doctor=doctor_id)
        return queryset

class AvailableTimeViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.AvailableTime.objects.all()
    serializer_class = serializers.AvailableTimeSerializers
    filter_backends = [AvailableTimeForSpacificeDoctor]

class SpecializationViewset(viewsets.ModelViewSet):
    queryset = models.Specialization.objects.all()
    serializer_class = serializers.SpecializationSerializers

class ReviewViewset(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializers
