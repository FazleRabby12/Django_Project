from django.contrib import admin
from django.urls import path, include
from .import views
#from .views import Biography
from .views import Academic
from .views import Financial
from .views import User1
from .views import Course
from .views import Result
from .views import Item
from .views import Item1
from .views import Item3
from .views import RegisterAPI
from knox import views as knox_views
from .views import LoginAPI
from django.urls import path
#from .views import TestView
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
    path("Biographyt.html", views.Biographyt, name="Biographyt"),
    path("Academict.html", views.Academict, name="Academict"),
    path("Financialt.html", views.Financialt, name="Financialt"),
    #path("grade.html", views.grade, name="grade"),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path("login.html", views.login1, name="login1"),
   # path('', views.apiOverview, name='apiOverview'),
    path("logout.html", views.logout, name="logout"),
    path("register.html", views.register, name="register"),
    path('Courses.html', views.Courses, name="Courses"),
    path('search.html', views.search, name="search"),
    path('results.html', views.results, name="results"),
    path('Customert.html', views.Customert, name="Customert"),
    path('student.html', views.student, name="student"),
    path("AddAcademic.html", views.AddAcademic, name="AddAcademic"),
    path("AddFinancial.html", views.AddFinancial, name="AddFinancial"),
    path('AddCourse.html', views.AddCourse, name="AddCourse"),
    path('AddResult.html', views.AddResult, name="AddResult"),
    path('customer-list/', views.ShowAll, name='customer-list'),
    path('customer-detail/<str:pk>/', views.viewCustomer, name='customer-list'),
    path('student-biography/', views.studentBiography, name='student-biography'),
    path('student-biography/<str:pk>/', views.viewBiography, name='student-biography'),
    path('student-academic/', views.studentAcademic, name='student-academic'),
    path('student-academic/<str:pk>/', views.viewAcademic, name='student-academic'),
    path('student-financial/', views.studentFinancial, name='student-financial'),
    path('student-financial/<str:pk>/', views.viewFinancial, name='student-financial'),
    path('delete/<int:studentid>/', views.delete_data, name="delete_data"),
    path('delete_result/<str:pk>/', views.delete_result, name="delete_result"),
    path('delete_datas/<int:pk>/', views.delete_datas, name="delete_datas"),
    path('delete_datal/<str:pk>/', views.delete_datal, name="delete_datal"),
    path('delete_datai/<str:pk>/', views.delete_datai, name="delete_datai"),
    path('delete_datam/<str:pk>/', views.delete_datam, name="delete_datam"),
    path('delete_student/<str:pk>/', views.delete_student, name="delete_student"),
    path('delete_biography/<int:pk>/', views.delete_biography, name="delete_biography"),
    path('UpdateBiography<int:pk>/', views.UpdateBiography, name="UpdateBiography"),
    path('UpdateAcademic<int:pk>/', views.UpdateAcademic, name="UpdateAcademic"),
    path('UpdateFinancial<int:pk>/', views.UpdateFinancial, name="UpdateFinancial"),
    path('UpdateCourse<str:pk>/', views.UpdateCourse, name="UpdateCourse"),
    path('UpdateCustomer<str:pk>/', views.UpdateCustomer, name="UpdateCustomer"),
    path('UpdateResult<str:pk>/', views.UpdateResult, name="UpdateResult"),
    path('UpdateStudent<int:pk>/', views.UpdateStudent, name="UpdateStudent"),
    path('UpdateResult<str:pk>/', views.UpdateResult, name="UpdateResult"),
    path('add-product/', views.addProduct, name="add-prod"),
    path('add-product1/', views.addProduct1, name="add-prod1"), 
    path('add-product2/', views.addProduct2, name="add-prod2"),   
    #path('add2.html', views.addGrade, name="addGrade"),
    #path('', TestView.as_view(), name='test'),  
    #path('api/token/',obtain_auth_token, name='obtain-token'),
    #path('rest-auth/', include('rest_auth.urls')),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

]
