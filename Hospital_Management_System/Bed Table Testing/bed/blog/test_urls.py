from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import *


class TestUrls(SimpleTestCase):

  
    def test_bed_home_view_url_is_resolved(self):
        url = reverse('bed-home')
        self.assertEquals(resolve(url).func, bed_home_view)

 
    