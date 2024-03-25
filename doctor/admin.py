from typing import Any
from django.contrib import admin
from .models import Specialization , Designation , AvailableTime , Doctor , Review
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
# Register your models here.

class SpecializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name",]}
admin.site.register(Specialization,SpecializationAdmin)

class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name",]}
admin.site.register(Designation,DesignationAdmin)


admin.site.register(AvailableTime)

class DoctorAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','fee','meet_link','image']

    def first_name(self,obj):
        return obj.user.first_name
    
    def last_name(self,obj):
        return obj.user.last_name
    
    

admin.site.register(Doctor,DoctorAdmin)
admin.site.register(Review)
