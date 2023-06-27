from django.test import SimpleTestCase
from blog.views import *


class TestForms(SimpleTestCase):

  
    def Add_Doctor_from_valid_data(self):
        form =Add_Doctor(data={
            'doctorid':'125',
            'user_id':'234',
        })# testing with data
        self.assertTrue(form.is_valid()) # no errors if the form is valid


    