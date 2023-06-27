from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import *


class TestUrls(SimpleTestCase):

  
    def test_patient_home_view_url_is_resolved(self):
        url = reverse('patient-home')
        self.assertEquals(resolve(url).func, patient_home_view)


    