from django.urls import path

from .views import *

urlpatterns = [
   path('organ-home.html', organ_home_view, name='organ-home'),
  
]