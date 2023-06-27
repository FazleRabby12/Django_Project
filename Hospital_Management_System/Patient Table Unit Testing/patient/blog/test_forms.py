from django.test import SimpleTestCase
from blog.views import *


class TestForms(SimpleTestCase):

    def Add_Patient_from_valid_data(self):
        form =Add_Patient(data={
            'patient_id':'524',
            'patient_name':'yash',
        })# testing with data
        self.assertTrue(form.is_valid()) # no errors if the form is valid

   