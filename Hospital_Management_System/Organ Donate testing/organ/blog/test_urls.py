from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import *


class TestUrls(SimpleTestCase):

    
    def test_organ_home_view_url_is_resolved(self):
        url = reverse('organ-home')
        self.assertEquals(resolve(url).func, organ_home_view)


    