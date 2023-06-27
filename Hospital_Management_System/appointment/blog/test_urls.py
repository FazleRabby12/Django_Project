from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import *


class TestUrls(SimpleTestCase):

    # Test the url for the patient's appointment home page
    def test_appointment_home_view_url_is_resolved(self):
        url = reverse('appointment-home')
        self.assertEquals(resolve(url).func, appointment_home_view)

    # Test the url for the doctor's appointment home page
    