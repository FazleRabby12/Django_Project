from django.contrib import admin
from django.urls import path, include
from .import views
from .views import Appointment
from .views import Bed
from .views import BloodDonate
from .views import Doctor
from .views import Patient
from .views import Nurse
from .views import OrganDonate
from .views import Medicine
from .views import Story
from .views import Test
from django.urls import path
from .views import RegisterAPI
from knox import views as knox_views
from .views import LoginAPI
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
   
    path("login.html", views.login, name="login"),
    path("logout.html", views.logout, name="logout"),
    path("register.html", views.register, name="register"),
    path("appointments.html", views.appointments, name="appointments"),
    path("beds.html", views.beds, name="beds"),
    path("nurses.html", views.nurses, name="nurses"),
    path("doctors.html", views.doctors, name="doctors"),
    path("bloods.html", views.bloods, name="bloods"),
    path("organs.html", views.organs, name="organs"),
    path("tests.html", views.tests, name="tests"),
    path("medicines.html", views.medicines, name="medicines"),
    path("patients.html", views.patients, name="patients"),
    path("stories.html", views.stories, name="stories"),
    path("AddAppointment.html", views.AddAppointment, name="AddAppointment"),
    path("users.html", views.users, name="users"),
    path("AddUser.html", views.AddUser, name="AddUser"),
    path("AddBed.html", views.AddBed, name="AddBed"),
    path("AddDoctor.html", views.AddDoctor, name="AddDoctor"),
    path("AddMedicine.html", views.AddMedicine, name="AddMedicine"),
    path("AddNurse.html", views.AddNurse, name="AddNurse"),
    path("AddOrgan.html", views.AddOrgan, name="AddOrgan"),
    path("AddPatient.html", views.AddPatient, name="AddPatient"),
    path("AddStory.html", views.AddStory, name="AddStory"),
    path("AddNurse.html", views.AddNurse, name="AddNurse"),
    path("AddTest.html", views.AddTest, name="AddTest"),
    path("AddBlood.html", views.AddBlood, name="AddBlood"),
    path('UpdateAppointment<str:pk>', views.UpdateAppointment, name='UpdateAppointment'),
    path('delete_datas/<str:pk>/', views.delete_datas, name="delete_datas"),
    path('UpdateBed<int:pk>/', views.UpdateBed, name="UpdateBed"),
    path('delete_datam/<int:pk>/', views.delete_datam, name="delete_datam"),
    path('UpdateDoctor<int:pk>/', views.UpdateDoctor, name="UpdateDoctor"),
    path('delete_doctor/<int:pk>/', views.delete_doctor, name="deletedoctor"),
    path('UpdateBlood<int:pk>/', views.UpdateBlood, name="UpdateBlood"),
    path('delete_blood/<int:pk>/', views.delete_blood, name="delete_blood"),
    path('UpdateMedicine<int:pk>/', views.UpdateMedicine, name="UpdateMedicine"),
    path('delete_medicine/<int:pk>/', views.delete_medicine, name="delete_medicine"),
    path('UpdateNurse<int:pk>/', views.UpdateNurse, name="UpdateNurse"),
    path('delete_nurse/<int:pk>/', views.delete_nurse, name="delete_nurse"),
    path('UpdateOrgan<int:pk>/', views.UpdateOrgan, name="UpdateOrgan"),
    path('delete_organ/<int:pk>/', views.delete_organ, name="delete_organ"),
    path('UpdatePatient<int:pk>/', views.UpdatePatient, name="UpdatePatient"),
    path('delete_patient/<int:pk>/', views.delete_patient, name="delete_patient"),
    path('UpdateStory<int:pk>/', views.UpdateStory, name="UpdateStory"),
    path('delete_story/<int:pk>/', views.delete_story, name="delete_story"),
    path('UpdateTest<int:pk>/', views.UpdateTest, name="UpdateTest"),
    path('delete_test/<int:pk>/', views.delete_test, name="delete_test"),
    path('UpdateUser<int:pk>/', views.UpdateUser, name="UpdateUser"),
    path('delete_user/<int:pk>/', views.delete_user, name="delete_user"),
  
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

]
