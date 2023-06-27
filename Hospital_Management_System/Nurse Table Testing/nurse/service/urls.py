from django.urls import path

from .views import *

urlpatterns = [
    path('nurse-home.html', nurse_home_view, name='nurse-home'),
  
]