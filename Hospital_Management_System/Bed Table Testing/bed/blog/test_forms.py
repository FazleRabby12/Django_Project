from django.test import SimpleTestCase
from blog.views import *


class TestForms(SimpleTestCase):

    def Add_Bed_from_valid_data(self):
        form =Add_Bed(data={
            'bed_id':'24',
            'bed_type':'ICU',
        })# testing with data
        self.assertTrue(form.is_valid()) # no errors if the form is valid

