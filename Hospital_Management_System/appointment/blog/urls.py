from django.urls import path

from .views import *

urlpatterns = [
    path('appointment-home.html', appointment_home_view, name='appointment-home'),
  
]