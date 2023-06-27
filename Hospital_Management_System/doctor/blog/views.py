from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required



from .forms import *
from .models import Doctor




@login_required(login_url='login')  # redirects to login if user is not logged in


def doctor_home_view(request):
    """
    This is a view for the patient to see their current appointments
    :param request: the HttpRequest
    :return: a rendered page
    This view is only accessible to logged in users who are patients.
    Patients will be able to see their upcoming, pending, canceled and completed appointments on this page.
    """
    user = request.user  # get current user from request
    #doctor = Doctor.objects.get(user=user)  # get current patient from user
    
    
    return render(request, 'doctor-home.html')  # render the page

