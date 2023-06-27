
from django.db import models

import datetime
import os
# Create your models here.


def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)


class Item(models.Model):

    bin = models.CharField(max_length=8, primary_key=True)  # Field name made lowercase.
    organizationname = models.CharField(max_length=20, blank=True, null=True)  # Field name made lowercase.
    organizationtype = models.CharField(max_length=15, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=20, blank=True, null=True)  # Field name made lowercase.
    image = models.ImageField(upload_to=filepath, null=True, blank=True)
    need_info = models.CharField(max_length=100, blank=True, null=True)

class Item1(models.Model):
    studentid = models.CharField(max_length=10, primary_key=True)  # Field name made lowercase.
    studentname = models.CharField( max_length=50)  # Field name made lowercase.
    image = models.FileField(upload_to=filepath, null=True, blank=True)  # Field name made lowercase.
    age = models.CharField(max_length=2)  # Field name made lowercase.
    bloodgroup = models.CharField(max_length=3)  # Field name made lowercase.
    nid_no = models.CharField(max_length=17)  # Field name made lowercase.
    email = models.CharField(max_length=30)  # Field name made lowercase.
    fathername = models.CharField(max_length=50)  # Field name made lowercase.
    nid_no_of_father = models.CharField(max_length=17)  # Field name made lowercase.
    mothername = models.CharField(max_length=50)  # Field name made lowercase.
    nid_no_of_mother = models.CharField(max_length=17)  # Field name made lowercase.


class Item3(models.Model):

    studentid = models.CharField(max_length=10, primary_key=True)  # Field name made lowercase.
    studentname = models.CharField( max_length=50)  # Field name made lowercase.
    organizationtype = models.CharField(max_length=15, blank=True, null=True)  # Field name made lowercase.
    image = models.FileField(upload_to=filepath, null=True, blank=True)  # Field name made lowercase.
    email = models.CharField(max_length=30)  # Field name made lowercase.
    biographic_info = models.CharField(max_length=200)  # Field name made lowercase.
    academic_info = models.CharField(max_length=200)  # Field name made lowercase.
    financial_info = models.CharField(max_length=200)  # Field name made lowercase.


class User1(models.Model):
    username = models.CharField(max_length=30)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    repassword = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'service_user'



class Academic(models.Model):
    studentid = models.IntegerField(db_column='StudentId', primary_key=True)  # Field name made lowercase.
    school = models.CharField(db_column='School', max_length=45)  # Field name made lowercase.
    college = models.CharField(db_column='College', max_length=45)  # Field name made lowercase.
    ssc_o_level_gpa = models.FloatField(db_column='SSC/O_Level_GPA')  # Field name made lowercase. Field renamed to remove unsuitable characters.      
    hsc_a_level_gpa = models.FloatField(db_column='HSC/A_Level_GPA')  # Field name made lowercase. Field renamed to remove unsuitable characters.      
    dateofenrolling = models.DateField(db_column='DateOfEnrolling', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'academic'
    
    
def __str__(self):
    return self.studentid + ' ' + self. school + ' ' + self.college + ' ' + self.ssc_o_level_gpa + ' ' + self.hsc_a_level_gpa + ' ' + self.dateofenrolling  + ' ' + self. student_idcard_pic




class Course(models.Model):
    coursecode = models.CharField(db_column='CourseCode', max_length=8 , primary_key=True)  # Field name made lowercase.
    coursename = models.CharField(db_column='CourseName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    credit = models.FloatField(db_column='Credit')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'course'

def __str__(self):
    return self.coursecode + ' ' + self.coursename + ' ' + self.credit 




class Financial(models.Model):
    studentid = models.IntegerField(db_column='StudentId', primary_key=True)  # Field name made lowercase.
    payableamount = models.IntegerField(db_column='PayableAmount')  # Field name made lowercase.
    paidamount = models.IntegerField(db_column='PaidAmount', blank=True, null=True)  # Field name made lowercase.
    f_income = models.IntegerField(db_column='F_Income', blank=True, null=True)  # Field name made lowercase.
    m_income = models.IntegerField(db_column='M_Income', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'financial'

def __str__(self):
    return self.studentid + ' ' + self.payableamount + ' ' + self.paidamount + ' ' + self.f_income + ' ' + self.m_income 





class Result(models.Model):
    studentid = models.IntegerField(db_column='StudentId', primary_key=True)  # Field name made lowercase.
    semester = models.CharField(db_column='Semester', max_length=20)  # Field name made lowercase.
    coursecode = models.CharField(db_column='CourseCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    course_grade = models.FloatField(db_column='Course_Grade')  # Field name made lowercase.
    credit = models.FloatField(db_column='Credit')  # Field name made lowercase.
    cgpa = models.FloatField(db_column='CGPA')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'result'

def __str__(self):
    return self.studentid + ' ' + self.semester + ' ' + self.coursecode+ ' ' + self.course_grade + ' ' + self.credit + ' ' + self.cgpa