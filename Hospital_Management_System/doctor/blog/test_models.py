from unittest import TestCase
from blog.models import Doctor
from .models import User



class DoctorTest(TestCase):

    def setUp(self):
        # Creating a user type object
        self.user = User.objects.all()
       
    

    def test_content(self):
        # Creating an doctor type object
        doctor = Doctor.objects.create(doctorid='123',
                                                user_id='154',
                                                contact_num='01745678903',
                                                email='rifat@gamil.com',
                                                meet_link='asadfeghh5')


        expected_object_doctorid = doctor.doctorid
        expected_object_user_id = doctor.user_id 
        expected_object_contact_num = doctor.contact_num 
        expected_object_email = doctor.email
        expected_object_meet_link= doctor.meet_link 
       

        self.assertEquals(expected_object_doctorid, '123') 
        self.assertEquals(expected_object_user_id, '154') 
        self.assertEquals(expected_object_contact_num, '01745678903')
        self.assertEquals(expected_object_email, 'rifat@gamil.com')
        self.assertEquals(expected_object_meet_link, 'asadfeghh5') 
    

    # Function to delete the previously crested user
    def tearDown(self):
        self.user.delete()