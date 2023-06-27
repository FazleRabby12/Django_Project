from django.db import models

# Create your models here.

class Doctor(models.Model):
    doctorid = models.CharField(max_length=6)  # Field name made lowercase.
    user_id = models.CharField(max_length=10)
    doctor_name = models.CharField( max_length=15)  # Field name made lowercase.
    contact_num = models.CharField(max_length=11)
    email = models.CharField(max_length=30)
    meet_link = models.CharField(max_length=40)

def __str__(self):
    return self.doctorid + ' ' + self.user_id + ' ' + self.doctor_name + ' ' + self.contact_num + ' ' + self. email + ' ' + self.meet_link


class User(models.Model):
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

def __str__(self):
    return self.username

