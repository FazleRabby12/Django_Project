from django.db import models
from djnago.contrib.auth.models import U 



class Test(models.Model):
    test_id = models.CharField(max_length=6)
    patient_id = models.CharField(max_length=5)
    test_charge = models.IntegerField()