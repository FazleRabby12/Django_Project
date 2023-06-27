from django.db import models

# Create your models here.



class Patient(models.Model):
    patient_id = models.CharField(max_length=5)  # Field name made lowercase.
    patient_name = models.CharField(max_length=20)  # Field name made lowercase.
    contact_num = models.CharField(max_length=11)
    age = models.IntegerField()  # Field name made lowercase.
    address = models.CharField(max_length=50)  # Field name made lowercase.
    patient_blood_group = models.CharField(max_length=5)

def __str__(self):
    return self.patient_id + ' ' + self.patient_name + ' ' + self.contact_num + ' ' + self.age + ' ' + self.address + ' ' + self.patient_blood_group
    
    

class User(models.Model):
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

def __str__(self):
    return self.username

