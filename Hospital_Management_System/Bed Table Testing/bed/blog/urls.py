from django.urls import path

from .views import *

urlpatterns = [
   path('bed-home.html', bed_home_view, name='bed-home'),
  
]