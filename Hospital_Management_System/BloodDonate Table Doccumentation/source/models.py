
from django.db import models
from djnago.contrib.auth.models import U 




class BloodDonate(models.Model):
    patient_id = models.CharField(max_length=10)
    user_id = models.CharField(max_length=10)
    blood_group = models.CharField(max_length=5)
    contact_num = models.CharField(max_length=11)
    location = models.CharField(max_length=20)
    need_date = models.DateField()