
from django.db import models
from djnago.contrib.auth.models import U 


class Story(models.Model):
    patient_id = models.CharField(max_length=10)
    story_date = models.DateField()
    comment = models.CharField(max_length=200)
