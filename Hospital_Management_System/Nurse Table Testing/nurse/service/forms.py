from django.core import validators
from django import forms
from .models import Nurse
from .models import User

class Add_Nurse(forms.ModelForm):
    class Meta:
     model=Nurse
     fields= ['nurse_id', 'nurse_name', 'floor_no']
     widgets= {
         'nurse_id': forms.TextInput(attrs={'class':'form-control'}),
         'nurse_name': forms.TextInput(attrs={'class':'form-control'}),
         'floor_no': forms.TextInput(attrs={'class':'form-control'}),
        
     }
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'