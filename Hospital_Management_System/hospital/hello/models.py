from django.db import models

# Create your models here.



class Appointment(models.Model):
    appointment_id = models.CharField(db_column='Appointment_Id', primary_key=True, max_length=15)  # Field name made lowercase.
    patient_id = models.CharField(max_length=10)
    doctor_id = models.CharField(max_length=10)
    appointment_date = models.DateTimeField(db_column='Appointment_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'appointment'


class Bed(models.Model):
    bed_id = models.CharField(primary_key=True, max_length=30)
    bed_type = models.CharField(db_column='Bed_Type', max_length=15)  # Field name made lowercase.
    vacancy = models.CharField(db_column='Vacancy', max_length=1)  # Field name made lowercase.
    bed_charge = models.IntegerField(db_column='Bed_Charge')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bed'


class BloodDonate(models.Model):
    patient_id = models.CharField(max_length=10, primary_key=True)
    user_id = models.CharField(max_length=10)
    blood_group = models.CharField(max_length=5)
    contact_num = models.CharField(max_length=11, blank=True, null=True)
    location = models.CharField(max_length=20, blank=True, null=True)
    need_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blood_donate'



class Doctor(models.Model):
    doctorid = models.CharField(db_column='Doctorid', primary_key=True, max_length=6)  # Field name made lowercase.
    user_id = models.CharField(max_length=10)
    doctor_name = models.CharField(db_column='Doctor_Name', max_length=15)  # Field name made lowercase.
    contact_num = models.CharField(max_length=11)
    email = models.CharField(max_length=30)
    meet_link = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'doctor'


class Medicine(models.Model):
    medicine_id = models.CharField(db_column='Medicine Id', primary_key=True, max_length=15)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    medicine_name = models.CharField(db_column='Medicine Name', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_id = models.CharField(max_length=10)
    expired_date = models.DateTimeField(db_column='Expired Date')  # Field name made lowercase. Field renamed to remove unsuitable characters.    
    price = models.SmallIntegerField(db_column='Price')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'medicine'


class Nurse(models.Model):
    nurse_id = models.CharField(db_column='Nurse_ID', primary_key=True, max_length=6)  # Field name made lowercase.
    nurse_name = models.CharField(db_column='Nurse_Name', max_length=15)  # Field name made lowercase.
    floor_no = models.IntegerField(db_column='Floor_No')  # Field name made lowercase.
   # bed_no = models.ForeignKey(Bed, models.DO_NOTHING, db_column='Bed_No')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nurse'


class OrganDonate(models.Model):
    patient_id = models.CharField(max_length=10, primary_key=True)
    user_id = models.CharField(max_length=10)
    blood_group = models.CharField(max_length=5)
    contact_num = models.CharField(max_length=11, blank=True, null=True)
    location = models.CharField(max_length=20, blank=True, null=True)
    need_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'organ_donate'


class Patient(models.Model):
    patient_id = models.CharField(db_column='Patient_Id', primary_key=True, max_length=5)  # Field name made lowercase.
    patient_name = models.CharField(db_column='Patient_Name', max_length=20)  # Field name made lowercase.
    contact_num = models.CharField(max_length=11)
    age = models.IntegerField(db_column='Age')  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=50)  # Field name made lowercase.
    patient_blood_group = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'patient'


class Test(models.Model):
    test_id = models.CharField(db_column='Test_Id', primary_key=True, max_length=6)  # Field name made lowercase.
    patient_id = models.CharField(db_column='Patient_ID', max_length=5)  # Field name made lowercase.
    test_charge = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'test'

class Story(models.Model):
    patient_id = models.CharField(max_length=10, primary_key=True)
    story_date = models.DateField()
    comment = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'story'


class User1(models.Model):
    username = models.CharField(max_length=30)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    repassword = models.CharField(max_length=30)


class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    blood_group = models.CharField(max_length=3)
    age = models.CharField(max_length=3)
    email = models.CharField(max_length=30)
    user_type = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'user'
