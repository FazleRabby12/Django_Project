from django.urls import path

from .views import *

urlpatterns = [
    path('doctor-home.html', doctor_home_view, name='doctor-home'),
  
]