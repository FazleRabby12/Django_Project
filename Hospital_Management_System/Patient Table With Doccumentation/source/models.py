
from django.db import models
from djnago.contrib.auth.models import U 



class Patient(models.Model):
    patient_id = models.CharField(max_length=5) 
    patient_name = models.CharField(max_length=20)
    contact_num = models.CharField(max_length=11)
    age = models.IntegerField()
    address = models.CharField(max_length=50)
    patient_blood_group = models.CharField(max_length=5)
