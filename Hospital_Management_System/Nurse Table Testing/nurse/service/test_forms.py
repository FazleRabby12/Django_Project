from django.test import SimpleTestCase
from service.views import *


class TestForms(SimpleTestCase):

  
    def Add_Nurse_from_valid_data(self):
        form =Add_Nurse(data={
            'nurse_id':'524',
            'user_name':'Akhi',
        })# testing with data
        self.assertTrue(form.is_valid()) # no errors if the form is valid


    