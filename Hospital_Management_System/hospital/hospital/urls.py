"""hospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from hello import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('login.html', views.login),
    path('logout.html', views.logout), 
    path("register.html", views.register), 
    path("appointments.html", views.appointments),
    path("beds.html", views.beds),
    path("nurses.html", views.nurses),
    path("doctors.html", views.doctors),
    path("bloods.html", views.bloods),
    path("organs.html", views.organs),
    path("tests.html", views.tests),
    path("medicines.html", views.medicines),
    path("patients.html", views.patients),
    path("stories.html", views.stories),
    path("AddAppointment.html", views.AddAppointment),
    path("AddBed.html", views.AddBed),
    path("AddDoctor.html", views.AddDoctor),
    path("AddNurse.html", views.AddNurse),
    path("AddOrgan.html", views.AddOrgan),
    path("AddPatient.html", views.AddPatient),
    path("AddStory.html", views.AddStory),
    path("AddNurse.html", views.AddNurse),
    path("AddTest.html", views.AddTest),
    path("AddMedicine.html", views.AddMedicine),
    path("AddBlood.html", views.AddBlood),
    path("users.html", views.users),
    path("AddUser.html", views.AddUser),
    path("UpdateAppointment<str:pk>/", views.UpdateAppointment),
    path('delete_datas/<str:pk>/', views.delete_datas),
    path('UpdateBed<int:pk>/', views.UpdateBed),
    path('delete_datam/<int:pk>/', views.delete_datam),
    path('UpdateDoctor<int:pk>/', views.UpdateDoctor),
    path('delete_doctor/<int:pk>/', views.delete_doctor),
    path('UpdateBlood<int:pk>/', views.UpdateBlood),
    path('delete_blood/<int:pk>/', views.delete_blood),
    path('UpdateMedicine<int:pk>/', views.UpdateMedicine),
    path('delete_medicine/<int:pk>/', views.delete_medicine),
    path('UpdateNurse<int:pk>/', views.UpdateNurse),
    path('delete_nurse/<int:pk>/', views.delete_nurse),
    path('UpdateOrgan<int:pk>/', views.UpdateOrgan),
    path('delete_organ/<int:pk>/', views.delete_organ),
    path('UpdatePatient<int:pk>/', views.UpdatePatient),
    path('delete_patient/<int:pk>/', views.delete_patient),
    path('UpdateStory<int:pk>/', views.UpdateStory),
    path('delete_story/<int:pk>/', views.delete_story),
    path('UpdateTest<int:pk>/', views.UpdateTest),
    path('delete_test/<int:pk>/', views.delete_test),
     path('UpdateUser<int:pk>/', views.UpdateUser),
    path('delete_user/<int:pk>/', views.delete_user),
    path('hello/', include('hello.urls')),

]



urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

