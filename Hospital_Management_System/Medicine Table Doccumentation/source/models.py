from django.db import models
from djnago.contrib.auth.models import U 




class Medicine(models.Model):
    medicine_id = models.CharField(max_length=15)
    medicine_name = models.CharField(max_length=20)
    patient_id = models.CharField(max_length=10)
    expired_date = models.DateTimeField()      
    price = models.SmallIntegerField()