from django.core import validators
from django import forms
from .models import Patient
from .models import User

class Add_Patient(forms.ModelForm):
    class Meta:
     model=Patient
     fields= ['patient_id', 'patient_name', 'contact_num', 'age', 'address', 'patient_blood_group']
     widgets= {
         'patient_id': forms.TextInput(attrs={'class':'form-control'}),
         'patient_name': forms.TextInput(attrs={'class':'form-control'}),
         'contact_num': forms.TextInput(attrs={'class':'form-control'}),
         'age': forms.TextInput(attrs={'class':'form-control'}),
         'address': forms.TextInput(attrs={'class':'form-control'}),
         'patient_blood_group': forms.TextInput(attrs={'class':'form-control'}),
     }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'