from django.core import validators
from django import forms
from .models import OrganDonate
from .models import User

class Add_OrganDonate(forms.ModelForm):
    class Meta:
     model=OrganDonate

     fields= ['patient_id', 'user_id', 'blood_group', 'contact_num','location','need_date']
     widgets= {
         'patient_id': forms.TextInput(attrs={'class':'form-control'}),
         'user_id': forms.TextInput(attrs={'class':'form-control'}),
         'blood_group': forms.TextInput(attrs={'class':'form-control'}),
         'contact_num': forms.TextInput(attrs={'class':'form-control'}),
         'location': forms.TextInput(attrs={'class':'form-control'}),
         'need_date': forms.DateInput(attrs={'class':'form-control'}),   
     } 
     
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'