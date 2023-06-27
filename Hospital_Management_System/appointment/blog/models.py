from django.db import models


class Appointment(models.Model):
    appointment_id = models.CharField( max_length=15)  # Field name made lowercase.
    patient_id = models.CharField(max_length=10)
    doctor_id = models.CharField(max_length=10)
    appointment_date = models.DateTimeField( blank=True,null=True)  # Field name made lowercase.

def __str__(self):
    return self.appointment_id + ' ' + self.patient_id + ' ' + self.doctor_id



class User(models.Model):
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

def __str__(self):
    return self.username

