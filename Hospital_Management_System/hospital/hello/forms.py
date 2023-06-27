from django.core import validators
from django import forms
from .models import Appointment
from .models import Bed
from .models import Medicine
from .models import Test
from .models import BloodDonate
from .models import OrganDonate
from .models import Nurse
from .models import Patient
from .models import Story
from .models import Doctor
from .models import User


# Field name made lowercase.

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
  

 

class Add_BloodDonate(forms.ModelForm):
    class Meta:
     model=BloodDonate
     fields= ['patient_id', 'user_id', 'blood_group', 'contact_num','location','need_date']
     widgets= {
         'patient_id': forms.TextInput(attrs={'class':'form-control'}),
         'user_id': forms.TextInput(attrs={'class':'form-control'}),
         'blood_group': forms.TextInput(attrs={'class':'form-control'}),
         'contact_num': forms.TextInput(attrs={'class':'form-control'}),
         'location': forms.TextInput(attrs={'class':'form-control'}),
         'need_date': forms.DateInput(attrs={'class':'form-control'}),
      
     } 


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
  
class Add_Medicine(forms.ModelForm):
    class Meta:
     model=Medicine
     fields= ['medicine_id', 'medicine_name', 'patient_id', 'expired_date', 'price']
     widgets= {
         'medicine_id': forms.TextInput(attrs={'class':'form-control'}),
         'medicine_name': forms.TextInput(attrs={'class':'form-control'}),
         'patient_id': forms.TextInput(attrs={'class':'form-control'}),
         'expired_date': forms.DateInput(attrs={'class':'form-control'}),
         'price': forms.TextInput(attrs={'class':'form-control'}),
     }

class Add_Nurse(forms.ModelForm):
    class Meta:
     model=Nurse
     fields= ['nurse_id', 'nurse_name', 'floor_no']
     widgets= {
         'nurse_id': forms.TextInput(attrs={'class':'form-control'}),
         'nurse_name': forms.TextInput(attrs={'class':'form-control'}),
         'floor_no': forms.TextInput(attrs={'class':'form-control'}),
        
     }



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

class Add_Test(forms.ModelForm):
    class Meta:
     model=Test
     fields= ['test_id', 'patient_id', 'test_charge']
     widgets= {
         'test_id': forms.TextInput(attrs={'class':'form-control'}),
         'patient_id': forms.TextInput(attrs={'class':'form-control'}),
         'test_charge': forms.TextInput(attrs={'class':'form-control'}),
        
     }


class Add_Story(forms.ModelForm):
    class Meta:
     model=Story
     fields= ['patient_id', 'story_date', 'comment']
     widgets= {
         'patient_id': forms.TextInput(attrs={'class':'form-control'}),
         'story_date': forms.TextInput(attrs={'class':'form-control'}),
         'comment': forms.TextInput(attrs={'class':'form-control'}),
        
     }


class Add_User(forms.ModelForm):
    class Meta:
     model=User
     fields= ['user_id', 'user_name', 'address', 'blood_group','age', 'email', 'user_type']
     widgets= {
         'user_id': forms.TextInput(attrs={'class':'form-control'}),
         'user_name': forms.TextInput(attrs={'class':'form-control'}),
         'address': forms.TextInput(attrs={'class':'form-control'}),
         'blood_group': forms.TextInput(attrs={'class':'form-control'}),
         'age': forms.TextInput(attrs={'class':'form-control'}),
         'email': forms.TextInput(attrs={'class':'form-control'}),
         'user_type': forms.TextInput(attrs={'class':'form-control'}),
     }
