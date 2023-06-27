"""Smart_Card URL Configuration

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
from service import views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('',views.Savevalue), 
    path('',views.savecheckboxvalues), 
    path('Biographyt.html', views.Biographyt),
    path('Academict.html', views.Academict),
    path('Financialt.html', views.Financialt),
    path('Customert.html', views.Customert),
    path('login.html', views.login1),
    path('logout.html', views.logout),
    path('Courses.html', views.Courses),
    path('student.html', views.student),
    path('results.html', views.results),
   # path('add2.html', views.addGrade), 
    path('AddAcademic.html', views.AddAcademic),
    path('AddFinancial.html', views.AddFinancial),
    path('AddCourse.html', views.AddCourse),
    path('AddResult.html', views.AddResult),
    path('register.html', views.register),
    #path('grade.html', views.grade),
    path('search.html', views.search),
    path('delete_result/<str:pk>/', views.delete_result),
    path('delete/<int:studentid>/', views.delete_data),
    path('delete_datas/<str:pk>/', views.delete_datas),
    path('delete_datam/<str:pk>/', views.delete_datam),
    path('delete_datam/<int:pk>/', views.delete_datai),
    path('delete_student/<str:pk>/', views.delete_student),
    path('delete_biography/<int:pk>/', views.delete_biography),
    path('delete_datal/<str:pk>/', views.delete_datal),
    path('UpdateBiography/<int:pk>/', views.UpdateBiography),
    path('UpdateBiography<int:pk>/', views.UpdateBiography),
    path('UpdateAcademic<int:pk>/', views.UpdateAcademic),
    path('UpdateStudent<int:pk>/', views.UpdateStudent),
    path('UpdateFinancial<int:pk>/', views.UpdateFinancial),
    path('UpdateCourse<str:pk>/', views.UpdateCourse),
    path('UpdateCustomer<str:pk>/', views.UpdateCustomer),
    path('UpdateResult<str:pk>/', views.UpdateResult),
    path('service/', include('service.urls')),

]


urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


   
