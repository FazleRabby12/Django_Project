from unittest import TestCase
from blog.models import OrganDonate
from .models import User



class OrganDonateTest(TestCase):

    def setUp(self):
        # Creating a user type object
        self.user = User.objects.all()
       
    

  
    def test_content(self):
       
        organ= OrganDonate.objects.create(patient_id='284',
                                            user_id='345',
                                            blood_group='A+',
                                            contact_num='01856790343',
                                            location='Kalabagan',
                                            need_date='2021-05-06')




        expected_object_patient_id =organ.patient_id
        expected_object_user_id = organ.user_id 
        expected_object_blood_group =organ.blood_group 
        expected_object_contact_num= organ.contact_num
        expected_object_location = organ.location 
        expected_object_need_date= organ.need_date


       

        self.assertEquals(expected_object_patient_id, '284',)
        self.assertEquals(expected_object_user_id, '345')
        self.assertEquals(expected_object_blood_group, 'A+')
        self.assertEquals(expected_object_contact_num, '01856790343')
        self.assertEquals(expected_object_location, 'Kalabagan')
        self.assertEquals(expected_object_need_date,'2021-05-06')
     

        

    

    # Function to delete the previously crested user
    def tearDown(self):
        self.user.delete()