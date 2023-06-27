from django.db import models

# Create your models here.


class OrganDonate(models.Model):
    patient_id = models.CharField(max_length=10)
    user_id = models.CharField(max_length=10)
    blood_group = models.CharField(max_length=5)
    contact_num = models.CharField(max_length=11)
    location = models.CharField(max_length=20)
    need_date = models.DateField()

def __str__(self):
    return self.patient_id + ' ' + self.user_id + ' ' + self.blood_group + ' ' + self.contact_num + ' ' + self.location + ' ' + self.need_date
    
    

class User(models.Model):
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

def __str__(self):
    return self.username

