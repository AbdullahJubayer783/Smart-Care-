from django.db import models
from patient.models import Patient
from doctor.models import Doctor , AvailableTime
# Create your models here.
APPOINTMENT_STATUS = [
    ('Completed','Completed'),
    ('Pending','Pending'),
    ('Running','Running'),
]

APPOINTMENT_TYPE = [
    ('Online','Online'),
    ('Offline','Offline'),
]

class Appointment(models.Model):
    patient = models.ForeignKey(Patient,on_delete = models.CASCADE)
    doctor = models.ForeignKey(Doctor,on_delete = models.CASCADE)
    appoint_status = models.CharField(choices = APPOINTMENT_STATUS , max_length = 40 , default='Pending')
    appoint_type = models.CharField(choices = APPOINTMENT_TYPE , max_length = 40)
    symptom = models.TextField()
    time = models.ForeignKey(AvailableTime,on_delete = models.CASCADE)
    cancle = models.BooleanField(default=False)

    def __str__(self):
        return f"Doctor: {self.doctor.user.first_name} | {self.patient.user.first_name}"

