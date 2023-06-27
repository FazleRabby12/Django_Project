from unittest import TestCase
from service.models import Nurse
from .models import User



class NurseTest(TestCase):

    def setUp(self):
        # Creating a user type object
        self.user = User.objects.all()
       
    

    # Function to test if the nurse model is created
    def test_content(self):
        
        nurse = Nurse.objects.create(nurse_id='222',
                                            nurse_name='akhi',
                                            floor_no='2')


        expected_object_nurse_id = nurse.nurse_id 
        expected_object_nurse_name = nurse.nurse_name 
        expected_object_floor_no = nurse.floor_no 

       

        self.assertEquals(expected_object_nurse_id, '222')
        self.assertEquals(expected_object_nurse_name, 'akhi') 
        self.assertEquals(expected_object_floor_no, '2')

    

    # Function to delete the previously crested user
    def tearDown(self):
        self.user.delete()