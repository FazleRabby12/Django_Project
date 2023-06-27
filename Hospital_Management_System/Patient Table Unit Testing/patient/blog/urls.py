from django.urls import path

from .views import *

urlpatterns = [
   path('patient-home.html', patient_home_view, name='patient-home'),
  
]