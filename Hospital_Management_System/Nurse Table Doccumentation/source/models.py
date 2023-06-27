
from django.db import models
from djnago.contrib.auth.models import U 




class Nurse(models.Model):
    nurse_id = models.CharField(max_length=6)  
    nurse_name = models.CharField( max_length=15)  
    floor_no = models.IntegerField() 