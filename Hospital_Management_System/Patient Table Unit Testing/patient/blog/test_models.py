from unittest import TestCase
from blog.models import Patient
from .models import User



class PatientTest(TestCase):

    def setUp(self):
        # Creating a user type object
        self.user = User.objects.all()
       
    

  
    def test_content(self):
       
        patient= Patient.objects.create(patient_id='230',
                                            patient_name='yash',
                                            contact_num='01745678945',
                                            age='25',
                                            address='Norda',
                                            patient_blood_group='A+')


        expected_object_patient_id = patient.patient_id
        expected_object_patient_name = patient.patient_name 
        expected_object_contact_num = patient.contact_num 
        expected_object_age = patient.age
        expected_object_address = patient.address 
        expected_object_patient_blood_group = patient.patient_blood_group

       

        self.assertEquals(expected_object_patient_id, '230')
        self.assertEquals(expected_object_patient_name, 'yash')
        self.assertEquals(expected_object_contact_num, '01745678945')
        self.assertEquals(expected_object_age, '25')
        self.assertEquals(expected_object_address, 'Norda')
        self.assertEquals(expected_object_patient_blood_group, 'A+')

        

    

    # Function to delete the previously crested user
    def tearDown(self):
        self.user.delete()