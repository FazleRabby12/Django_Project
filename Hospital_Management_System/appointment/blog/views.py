from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

#from user_control.decorators import show_to_doctor, show_to_patient

from .forms import *
from .models import Appointment
#from user_control.models import Appointment



@login_required(login_url='login')  # redirects to login if user is not logged in
 # accessible to patients only
def appointment_home_view(request):
    """
    This is a view for the patient to see their current appointments
    :param request: the HttpRequest
    :return: a rendered page
    This view is only accessible to logged in users who are patients.
    Patients will be able to see their upcoming, pending, canceled and completed appointments on this page.
    """
    user = request.user  # get current user from request
    appointment = Appointment.objects.get(user=user)  # get current patient from user
    appointments = Appointment.objects.filter(appointment=appointment)  # get all appointments for current patient
    pending_appointments = [appointment for appointment in appointments
                            if appointment.is_accepted == False
                            and appointment.is_canceled == False
                            and appointment.is_complete == False]  # get all pending appointments
    upcoming_appointments = [appointment for appointment in appointments
                             if appointment.is_accepted == True
                             and appointment.is_canceled == False
                             and appointment.is_complete == False]  # get all upcoming appointments
    rejected_appointments = [appointment for appointment in appointments
                             if appointment.is_accepted == False
                             and appointment.is_canceled == True
                             and appointment.is_complete == False]  # get all rejected appointments
    completed_appointments = [appointment for appointment in appointments
                              if appointment.is_accepted == True
                              and appointment.is_canceled == False
                              and appointment.is_complete == True]  # get all completed appointments

    context = {  # create context to pass to frontend
        'pending_appointments': pending_appointments,
        'upcoming_appointments': upcoming_appointments,
        'rejected_appointments': rejected_appointments,
        'completed_appointments': completed_appointments,
    }
    return render(request, 'appointment-home.html', context)  # render the page

