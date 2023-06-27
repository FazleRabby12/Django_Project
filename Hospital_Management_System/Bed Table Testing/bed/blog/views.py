from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required



from .forms import *
from .models import Bed




@login_required(login_url='login') 


def bed_home_view(request):
    """
    This is a view for the patient to see their current appointments
    :param request: the HttpRequest
    :return: a rendered page
    This view is only accessible to logged in users who are patients.
    Patients will be able to see their upcoming, pending, canceled and completed appointments on this page.
    """
    user = request.user  
    
    
    return render(request, 'bed-home.html')  # render the page

