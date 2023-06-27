from django.test import SimpleTestCase
from blog.views import *


class TestForms(SimpleTestCase):

    def Add_OrganDonate_from_valid_data(self):
        form =Add_OrganDonate(data={
            'patient_id':'23',
            'location':'Dhanmondi',
        })# testing with data
        self.assertTrue(form.is_valid()) # no errors if the form is valid

  