from django.contrib import admin
from .models import Appointment
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
# Register your models here.

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['doctor_name','patient_name','appoint_status','appoint_type','symptom','appoint_type','time','cancle']

    def doctor_name(self,obj):
        return obj.patient.user.first_name
    def patient_name(self,obj):
        return obj.doctor.user.first_name
    
    def save_model(self, request, obj, form, change):
        obj.save()
        print('Inside func')
        if obj.appoint_status == 'Running' and obj.appoint_type == 'Online':
            print('Inside running appointment')
            email_subject = "Confirm email"
            email_body = render_to_string('admin_email.html',{'patient':obj.patient.user,'doctor':obj.doctor})
            email = EmailMultiAlternatives(email_subject,'',to=[obj.patient.user.email])
            email.attach_alternative(email_body,"text/html")
            email.send()
    
admin.site.register(Appointment,AppointmentAdmin)