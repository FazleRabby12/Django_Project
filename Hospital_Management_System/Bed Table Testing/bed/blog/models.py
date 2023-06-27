from django.db import models

# Create your models here.



class Bed(models.Model):
    bed_id = models.CharField(max_length=30)
    bed_type = models.CharField(max_length=15)  # Field name made lowercase.
    vacancy = models.CharField(max_length=5)  # Field name made lowercase.
    bed_charge = models.IntegerField()  # Field name made lowercase.


def __str__(self):
    return self.bed_id + ' ' + self.bed_type + ' ' + self.vacancy + ' ' + self.bed_charge
    
    

class User(models.Model):
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

def __str__(self):
    return self.username

