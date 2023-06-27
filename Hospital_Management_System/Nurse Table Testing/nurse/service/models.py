from django.db import models

# Create your models here.



class Nurse(models.Model):
    nurse_id = models.CharField(max_length=6)  # Field name made lowercase.
    nurse_name = models.CharField(max_length=15)  # Field name made lowercase.
    floor_no = models.IntegerField()

def __str__(self):
    return self.nurse_id + ' ' + self.nurse_name + ' ' + self.floor_no
    

class User(models.Model):
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

def __str__(self):
    return self.username

