from django.test import SimpleTestCase
from django.urls import reverse, resolve
from service.views import *


class TestUrls(SimpleTestCase):

 
    def test_nurse_home_view_url_is_resolved(self):
        url = reverse('nurse-home')
        self.assertEquals(resolve(url).func, nurse_home_view)

    