from django.core import validators
from django import forms
from .models import Academic
#from .models import Biography
from .models import Financial
from .models import Course
from .models import Result
from .models import Item
from .models import Item1
from .models import Item3





class Add_Academic(forms.ModelForm):
    class Meta:
     model=Academic
     fields= ['school', 'college',  'ssc_o_level_gpa', 'hsc_a_level_gpa',  'dateofenrolling' ]
     widgets= {
         'studentid': forms.TextInput(attrs={'class':'form-control'}),
         'school': forms.TextInput(attrs={'class':'form-control'}),
         'college': forms.TextInput(attrs={'class':'form-control'}),
         'ssc_o_level_gpa': forms.TextInput(attrs={'class':'form-control'}),
         'hsc_a_level_gpa': forms.TextInput(attrs={'class':'form-control'}),
         'dateofenrolling': forms.DateInput(attrs={'class':'form-control'}),
         
     }
  

# Field name made lowercase.

class Add_Biography(forms.ModelForm):
    class Meta:
     model=Item1
     fields= ['studentname', 'image', 'age', 'bloodgroup', 'nid_no', 'email', 'fathername', 'nid_no_of_father','mothername','nid_no_of_mother']
     widgets= {
         'studentid': forms.TextInput(attrs={'class':'form-control'}),
         'studentname': forms.TextInput(attrs={'class':'form-control'}),
         'age': forms.TextInput(attrs={'class':'form-control'}),
         'bloodgroup': forms.TextInput(attrs={'class':'form-control'}),
         'nid_no': forms.TextInput(attrs={'class':'form-control'}),
         'email': forms.TextInput(attrs={'class':'form-control'}),
         'fathername': forms.TextInput(attrs={'class':'form-control'}),
         'nid_no_of_father': forms.TextInput(attrs={'class':'form-control'}),
         'mothername': forms.TextInput(attrs={'class':'form-control'}),
         'nid_no_of_mother': forms.TextInput(attrs={'class':'form-control'}),
     }

class Add_Biography(forms.ModelForm):
    class Meta:
     model=Item1
     fields= ['studentid','studentname', 'image', 'age', 'bloodgroup', 'nid_no', 'email', 'fathername', 'nid_no_of_father','mothername','nid_no_of_mother']
     widgets= {
         'studentid': forms.TextInput(attrs={'class':'form-control'}),
         'studentname': forms.TextInput(attrs={'class':'form-control'}),
         'age': forms.TextInput(attrs={'class':'form-control'}),
         'bloodgroup': forms.TextInput(attrs={'class':'form-control'}),
         'nid_no': forms.TextInput(attrs={'class':'form-control'}),
         'email': forms.TextInput(attrs={'class':'form-control'}),
         'fathername': forms.TextInput(attrs={'class':'form-control'}),
         'nid_no_of_father': forms.TextInput(attrs={'class':'form-control'}),
         'mothername': forms.TextInput(attrs={'class':'form-control'}),
         'nid_no_of_mother': forms.TextInput(attrs={'class':'form-control'}),
     }

class Add_Student(forms.ModelForm):
    class Meta:
     model=Item3
     fields= ['studentid','studentname', 'organizationtype','image', 'email', 'biographic_info', 'academic_info', 'financial_info']
     widgets= {
         'studentid': forms.TextInput(attrs={'class':'form-control'}),
         'studentname': forms.TextInput(attrs={'class':'form-control'}),
         'organizationtype': forms.TextInput(attrs={'class':'form-control'}),
         'email': forms.TextInput(attrs={'class':'form-control'}),
         'biographic_info': forms.TextInput(attrs={'class':'form-control'}),
         'academic_info': forms.TextInput(attrs={'class':'form-control'}),
         'financial_info': forms.TextInput(attrs={'class':'form-control'}),
         'nid_no_of_mother': forms.TextInput(attrs={'class':'form-control'}),
     }

class Add_Financial(forms.ModelForm):
    class Meta:
     model=Financial
     fields= ['payableamount',  'paidamount', 'f_income','m_income' ]
     widgets= {
        # 'studentid': forms.TextInput(attrs={'class':'form-control'}),
         'payableamount': forms.TextInput(attrs={'class':'form-control'}),
         'paidamount': forms.TextInput(attrs={'class':'form-control'}),
         'f_income': forms.TextInput(attrs={'class':'form-control'}),
         'm_income': forms.TextInput(attrs={'class':'form-control'}),
        
     }


class Add_Customer(forms.ModelForm):  
   class Meta:
     model= Item
       
     fields= ['bin','organizationname', 'organizationtype','email','image','need_info']
     widgets= {
         'bin': forms.TextInput(attrs={'class':'form-control'}),
         'organizationname': forms.TextInput(attrs={'class':'form-control'}),
         'organizationtype': forms.TextInput(attrs={'class':'form-control'}),
         'email': forms.TextInput(attrs={'class':'form-control'}),
         'need_info': forms.TextInput(attrs={'class':'form-control'}),
        
     }




class Add_Course(forms.ModelForm):
    class Meta:
     model=Course
     fields= [ 'coursecode','coursename','credit' ]
     widgets= {
         'coursecode': forms.TextInput(attrs={'class':'form-control'}),
         'coursename': forms.TextInput(attrs={'class':'form-control'}),
         'credit': forms.TextInput(attrs={'class':'form-control'}),
        
     }
     

class Add_Result(forms.ModelForm):
    class Meta:
     model=Result

     fields= ['studentid','semester','coursecode','course_grade','credit','cgpa' ]
     widgets= {
         'studentid': forms.TextInput(attrs={'class':'form-control'}),
         'semester': forms.TextInput(attrs={'class':'form-control'}),
         'coursecode': forms.TextInput(attrs={'class':'form-control'}),
         'course_grade': forms.TextInput(attrs={'class':'form-control'}),
         'credit': forms.TextInput(attrs={'class':'form-control'}),
         'cgpa': forms.TextInput(attrs={'class':'form-control'}),
  
      
     }

 

