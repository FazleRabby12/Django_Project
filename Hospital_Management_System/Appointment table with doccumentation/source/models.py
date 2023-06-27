
from django.db import models
from djnago.contrib.auth.models import U 

class Appointment(models.Model):
    appointment_id = models.CharField( max_length=15)  # Field name made lowercase.
    patient_id = models.CharField(max_length=10)
    doctor_id = models.CharField(max_length=10)
    appointment_date = models.DateTimeField()  # Field name made lowercase.ss