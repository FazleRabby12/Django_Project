from unittest import TestCase
from blog.models import Bed
from .models import User



class BedTest(TestCase):

    def setUp(self):
        # Creating a user type object
        self.user = User.objects.all()
       
    

  
    def test_content(self):
       
        bed= Bed.objects.create( bed_id='28',
                                            bed_type='ICU',
                                            vacancy='yes',
                                            bed_charge='15000')




        expected_object_bed_id = bed.bed_id
        expected_object_bed_type = bed.bed_type 
        expected_object_vacancy = bed.vacancy 
        expected_object_bed_charge= bed.bed_charge


       

        self.assertEquals(expected_object_bed_id, '28')
        self.assertEquals(expected_object_bed_type, 'ICU')
        self.assertEquals(expected_object_vacancy, 'yes')
        self.assertEquals(expected_object_bed_charge, '15000')
     

        

    

    # Function to delete the previously crested user
    def tearDown(self):
        self.user.delete()