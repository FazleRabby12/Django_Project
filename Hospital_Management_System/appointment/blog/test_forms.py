from django.test import SimpleTestCase
from blog.views import *


class TestForms(SimpleTestCase):

    # Test the form for adding a new appointment with valid data
    def Add_Appointment_from_valid_data(self):
        form = Add_Appointment(data={
            'appointment_id':'1234',
             'patient_id':'234',
        })# testing with data
        self.assertTrue(form.is_valid()) # no errors if the form is valid

    # Test the form for adding a new appointment with invalid data
    