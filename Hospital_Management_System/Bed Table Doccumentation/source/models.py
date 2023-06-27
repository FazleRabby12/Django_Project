
from django.db import models
from djnago.contrib.auth.models import U 


class Bed(models.Model):
    bed_id = models.CharField(max_length=30)
    bed_type = models.CharField( max_length=15)  
    vacancy = models.CharField(max_length=1)  
    bed_charge = models.IntegerField() 
