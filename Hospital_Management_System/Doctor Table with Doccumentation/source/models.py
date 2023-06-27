
from django.db import models
from djnago.contrib.auth.models import U 



class Doctor(models.Model):
    doctorid = models.CharField(max_length=6)  
    user_id = models.CharField(max_length=10)
    doctor_name = models.CharField(max_length=15)  
    contact_num = models.CharField(max_length=11)
    email = models.CharField(max_length=30)
    meet_link = models.CharField(max_length=40)
