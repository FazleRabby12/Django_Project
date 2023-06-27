from django.core import validators
from django import forms
from .models import Doctor
from .models import User

class Add_Doctor(forms.ModelForm):
    class Meta:
     model=Doctor
     fields= ['doctorid', 'user_id', 'doctor_name', 'contact_num', 'email', 'meet_link']
     widgets= {
         'doctorid': forms.TextInput(attrs={'class':'form-control'}),
         'user_id': forms.TextInput(attrs={'class':'form-control'}),
         'doctor_name': forms.TextInput(attrs={'class':'form-control'}),
         'contact_num': forms.TextInput(attrs={'class':'form-control'}),
         'email': forms.TextInput(attrs={'class':'form-control'}),
         'meet_link': forms.TextInput(attrs={'class':'form-control'}),
     }
  
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'