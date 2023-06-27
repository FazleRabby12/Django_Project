
from django.db import models
from djnago.contrib.auth.models import U 




class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    blood_group = models.CharField(max_length=3)
    age = models.CharField(max_length=3)
    email = models.CharField(max_length=30)
    user_type = models.CharField(max_length=10)