from django.core import validators
from django import forms
from .models import Appointment
from .models import User


class Add_Appointment(forms.ModelForm):
    class Meta:
     model=Appointment
     fields= ['appointment_id', 'patient_id', 'doctor_id', 'appointment_date']
     widgets= {
         'appointment_id': forms.TextInput(attrs={'class':'form-control'}),
         'patient_id': forms.TextInput(attrs={'class':'form-control'}),
         'doctor_id': forms.TextInput(attrs={'class':'form-control'}),
         'appointment_date': forms.DateInput(attrs={'class':'form-control'}),
      

     }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'