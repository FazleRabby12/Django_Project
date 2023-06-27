from django.core import validators
from django import forms
from .models import Bed
from .models import User


class Add_Bed(forms.ModelForm):
    class Meta:
     model=Bed
     fields= ['bed_id', 'bed_type', 'vacancy', 'bed_charge']
     widgets= {
         'appointment_id': forms.TextInput(attrs={'class':'form-control'}),
         'bed_type': forms.TextInput(attrs={'class':'form-control'}),
         'vacancy': forms.TextInput(attrs={'class':'form-control'}),
         'bed_charge': forms.TextInput(attrs={'class':'form-control'}),
      
     }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'