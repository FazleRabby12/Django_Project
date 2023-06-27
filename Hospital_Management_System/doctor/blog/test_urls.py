from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import *


class TestUrls(SimpleTestCase):

   
    def test_doctor_home_view_url_is_resolved(self):
        url = reverse('doctor-home')
        self.assertEquals(resolve(url).func, doctor_home_view)


    