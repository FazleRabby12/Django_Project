from django.db import connection
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.shortcuts import render, HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Academic
from .models import Financial
from .models import  Result
from .models import Course

from .models import User1
from .serializers import Item3Serializer
from .serializers import AcademicSerializer
from .serializers import Item1Serializer
from .serializers import FinancialSerializer

from .models import Item
from .models import Item1
from .models import Item3
import mysql.connector
from operator import itemgetter
from django.contrib import messages
from .forms import Add_Academic
from .forms import Add_Biography
from .forms import Add_Financial
from .forms import Add_Course
from .forms import Add_Result
#from .forms import Add_Customer
#from .forms import Add_Student
import os

from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })


from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

"""
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


class TestView(APIView):
    
    permission_classes= (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        qs=Post.objects.all()
        post=qs.first()
        serializer= PostSerializer(post)
        return Response(serializer.data)
        
    def post(self, request, *args, **kwargs):
        serializer=PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

"""

# Create your views here.
"""@api_view(['GET'])
def apiOverview(request):
    service_urls={
        'List': '/customer-list/',
        'Detail View':'/customer-details/<int:id>',
        'Create':'/customer-create',
        'Update':'/customer-update/<int:id>',
        'Delete':'/customer-details/<int:id>'

    }
    return Response(service_urls);
"""

@api_view(['GET'])
def ShowAll(request):

    products=Item3.objects.all()
    serializer= Item3Serializer(products, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def viewCustomer(request, pk):

    customer=Item3.objects.get(studentid=pk)
    serializer= Item3Serializer(customer, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def studentBiography(request):

    products=Item1.objects.all()
    serializer= Item1Serializer(products, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def viewBiography(request, pk):

    customer=Item1.objects.get(studentid=pk)
    serializer= Item1Serializer(customer, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def studentAcademic(request):

    products=Academic.objects.all()
    serializer= AcademicSerializer(products, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def viewAcademic(request, pk):

    customer=Academic.objects.get(studentid=pk)
    serializer= AcademicSerializer(customer, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def studentFinancial(request):

    products=Financial.objects.all()
    serializer= FinancialSerializer(products, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def viewFinancial(request, pk):

    customer=Financial.objects.get(studentid=pk)
    serializer= FinancialSerializer(customer, many=False)
    return Response(serializer.data)



def index(request):

    return render(request,'index.html')

def search(request):

    #products=Item.objects.all()
    query = request.GET['query']
    products=Item.objects.filter(bin__icontains= query)
       
    context={
        'products': products
    }

    return render(request,'search.html', context)
    

def login1(req):
    con=mysql.connector.connect(host="localhost",user="root",password="",database='student_ekyc')
    cursor=con.cursor()
    con2=mysql.connector.connect(host="localhost",user="root",password="",database='student_ekyc')
    cursor2=con2.cursor()
    sqlcommand="select username from service_user"
    sqlcommand2="select password from service_user"
    cursor.execute(sqlcommand)
    cursor2.execute(sqlcommand2)

    u=[]
    p=[]

    for i in cursor:
        u.append(i)
    for j in cursor2:
        p.append(j) 
    res=list(map(itemgetter(0),u))
    res2=list(map(itemgetter(0),p))
    print(res)
    #print(p)

    if req.method=="POST":
        username=req.POST['username']
        password=req.POST['password']
        i=1
        k=len(res)
        while i<k:
                if res[i]==username and res2[i]==password:
                    return render(req,'index.html',{'username':username})
                    break
                i=i+1
        else:
          messages.info(req, "Check username or password")
          return redirect("/")
    
  

    return render(req, 'login.html')
    User1()
    

def logout(request):

    return render(request, 'logout.html')

    
def register(req):
    if req.method=="POST":
        user=User1()

        user.username=req.POST['username']
        user.fname=req.POST['fname']
        user.lname=req.POST['lname']
        user.password=req.POST['password']
        user.repassword=req.POST['repassword']
        if user.password!=user.repassword:
            return redirect('register')
        elif user.fname=="" or user.password=="":
            messages.info(req, 'some fields are empty')
            return redirect('register')
        else:
            user.save()
    return render(req, 'register.html')


def Biographyt(request):
     products=Item1.objects.all()

     context={
        'products': products
     }
     return render(request, 'Biographyt.html', context)

def addProduct(request):
    if request.method == "POST":
        prod = Item()
        prod.studentid = request.POST.get('studentid')
        prod.bin = request.POST.get('bin')
        prod.organizationname = request.POST.get('organizationname')
        prod.organizationtype = request.POST.get('organizationtype')
        prod.email = request.POST.get('email')
        prod.need_info = request.POST.get('need_info')

        if len(request.FILES) != 0:
            prod.image = request.FILES['image']

        prod.save()
        messages.success(request, "Product Added Successfully")
        return redirect('/')
    return render(request, 'add.html')


def addProduct1(request):
    if request.method == "POST":
        prod = Item1()
        prod.studentid = request.POST.get('studentid')
        prod.studentname = request.POST.get('studentname')
        prod.age = request.POST.get('age')
        prod.bloodgroup = request.POST.get('bloodgroup')
        prod.nid_no = request.POST.get('nid_no')
        prod.email = request.POST.get('email')
        prod.fathername = request.POST.get('fathername')
        prod.nid_no_of_father = request.POST.get('nid_no_of_father')
        prod.mothername = request.POST.get('mothername')
        prod.nid_no_of_mother = request.POST.get('nid_no_of_mother')

        if len(request.FILES) != 0:
            prod.image = request.FILES['image']

        prod.save()
        messages.success(request, "Biography Added Successfully")
        return redirect('/')
    return render(request, 'add1.html')

def addProduct2(request):
    if request.method == "POST":
        prod = Item3()
        prod.studentid = request.POST.get('studentid')
        prod.studentname = request.POST.get('studentname')
        prod.organizationtype = request.POST.get('organizationtype')
        prod.email = request.POST.get('email')
        prod.biographic_info = request.POST.get('biographic_info')
        prod.academic_info = request.POST.get('academic_info')
        prod.financial_info = request.POST.get('financial_info')
      

        if len(request.FILES) != 0:
            prod.image = request.FILES['image']

        prod.save()
        messages.success(request, "Student Information Added Successfully")
        return redirect('/')
    return render(request, 'add2.html')



def Academict(request):
    academics=Academic.objects.all()

    context={
        'academics': academics
    }
    return render(request, 'Academict.html', context)

def Financialt(request):
    financials=Financial.objects.all()

    context={
        'financials': financials
    }
    return render(request, 'Financialt.html', context)

def Courses(request):
    coursest=Course.objects.all()

    context={
        'coursest': coursest
    }
    return render(request, 'Courses.html', context)

def results(request):
    
    resultst=Result.objects.all()

    context={
        'resultst': resultst
    }
    return render(request, 'results.html', context)



def Customert(request):

    products=Item.objects.all()

    context={
        'products': products
    }
    return render(request, 'Customert.html', context)


def student(request):

    stu=Item3.objects.all()

    context={
        'stu': stu
    }
    return render(request, 'student.html', context)



def AddAcademic(request):
    if request.method== 'POST':
        fm=Add_Academic(request.POST)
        if fm.is_valid():
            fm.save()
            fm=Add_Academic()
    else:
      fm=Add_Academic()
    return render(request, 'AddAcademic.html', {'form':fm})



def Savevalue(request):
    if request.method=='POST':
         if request.POST.get('need_info'):
            saverecord=Item()
            saverecord.need_info=request.POST.get('need_info')
            saverecord.save()
            return render(request, 'Customert.html')
    else:
        return render(request, 'Customert.html')

def savecheckboxvalues(request):
    if request.method=="POST":
        if request.POST.get('biographic_info') and request.POST.get('academic_info') and request.POST.get('financial_info'):
            savevalues=student()
            savevalues.biographic_info= request.POST.get('biographic_info')
            savevalues.academic_info= request.POST.get('academic_info')
            savevalues.financial_info= request.POST.get('financial_info')
            cursor=connection.cursor()
            cursor.execute("Call MultipleInsertrecords('"+savevalues.biographic_info+"','"+savevalues.academic_info+"','"+savevalues.academic_info+"')")
            return render(request, 'student.html')
    else:
        return render(request, 'student.html')

def AddBiography(request):
   
    if request.method== 'POST':
        fm=Add_Biography(request.POST)
        if fm.is_valid():
            fm.save()
            fm=Add_Biography()
    else:
      fm=Add_Biography()
 
    return render(request, 'AddBiography.html', {'form':fm})



def AddCourse(request):
   
    if request.method== 'POST':
        fm=Add_Course(request.POST)
        if fm.is_valid():
            fm.save()
            fm=Add_Course()
    else:
      fm=Add_Course()
 
    return render(request, 'AddCourse.html', {'form':fm})

def AddResult(request):
   
    if request.method== 'POST':
        fm=Add_Result(request.POST)
        if fm.is_valid():
            fm.save()
            fm=Add_Result()
    else:
      fm=Add_Result()
 
    return render(request, 'AddResult.html', {'form':fm})   

def UpdateBiography(request, pk):
   
        prod=Item1.objects.get(studentid=pk)

        if request.method== 'POST':
            if len(request.FILES) != 0:
                if len(prod.image) > 0:
                    os.remove(prod.image.path)
            
                prod.image = request.FILES['image']
            
            prod.studentid = request.POST.get('studentid')
            prod.studentname = request.POST.get('studentname')
            prod.age = request.POST.get('age')
            prod.bloodgroup = request.POST.get('bloodgroup')
            prod.nid_no = request.POST.get('nid_no')
            prod.email = request.POST.get('email')
            prod.fathername = request.POST.get('fathername')
            prod.nid_no_of_father = request.POST.get('nid_no_of_father')
            prod.mothername = request.POST.get('mothername')
            prod.nid_no_of_mother = request.POST.get('nid_no_of_mother')
            prod.save()
            messages.success(request, "Customer information updated Successfully")
            return redirect('/')
    

        context={'prod':prod}

        return render(request, 'UpdateBiography.html', context)

def UpdateCustomer(request, pk):
   
        prod=Item.objects.get(bin=pk)

        if request.method== 'POST':
            if len(request.FILES) != 0:
                if len(prod.image) > 0:
                    os.remove(prod.image.path)
            
                prod.image = request.FILES['image']
            
            prod.bin = request.POST.get('bin')
            prod.organizationname = request.POST.get('organizationname')
            prod.organizationtype = request.POST.get('organizationtype')
            prod.email = request.POST.get('email')
            prod.need_info = request.POST.get('need_info')
            prod.save()
            messages.success(request, "Customer information updated Successfully")
            return redirect('/')
    

        context={'prod':prod}

        return render(request, 'UpdateCustomer.html', context)

def UpdateAcademic(request, pk):
   
        pt=Academic.objects.get(studentid=pk)
        fm=Add_Academic(instance=pt)

        if request.method== 'POST':
            fm=Add_Academic(request.POST, instance=pt)
            if fm.is_valid():
                fm.save()
                return redirect('/')

        context={'form':fm}
        
    
        return render(request, 'UpdateAcademic.html', context)

def UpdateStudent(request, pk):
   
       
        prod=Item3.objects.get(studentid=pk)

        if request.method== 'POST':
            if len(request.FILES) != 0:
                if len(prod.image) > 0:
                    os.remove(prod.image.path)
            
                prod.image = request.FILES['image']
            
            prod.studentid = request.POST.get('studentid')
            prod.studentname = request.POST.get('studentname')
            prod.organizationtype = request.POST.get('organizationtype')
            prod.email = request.POST.get('email')
            prod.biographic_info = request.POST.get('biographic_info')
            prod.academic_info = request.POST.get('academic_info')
            prod.financial_info = request.POST.get('financial_info')
            prod.save()
            messages.success(request, "Student information updated Successfully")
            return redirect('/')
    

        context={'prod':prod}

        return render(request, 'UpdateStudent.html', context)


def UpdateFinancial(request, pk):
   
        ps=Financial.objects.get(studentid=pk)
        fm=Add_Financial(instance=ps)

        if request.method== 'POST':
            fm=Add_Financial(request.POST, instance=ps)
            if fm.is_valid():
                fm.save()
                return redirect('/')

        context={'form':fm}
        
    
        return render(request, 'UpdateFinancial.html', context)


def UpdateCourse(request, pk):
   
        ps=Course.objects.get(coursecode=pk)
        fm=Add_Course(instance=ps)

        if request.method== 'POST':
            fm=Add_Course(request.POST, instance=ps)
            if fm.is_valid():
                fm.save()
                return redirect('/')

        context={'form':fm}
    
    
        return render(request, 'UpdateCourse.html', context)


def UpdateResult(request, pk):
   
        pf=Result.objects.get(studentid=pk)
        fm=Add_Result(instance=pf)

        if request.method== 'POST':
            fm=Add_Result(request.POST, instance=pf)
            if fm.is_valid():
                fm.save()
                return redirect('/')

        context={'form':fm}
        
    
        return render(request, 'UpdateResult.html', context)

def AddFinancial(request):
    if request.method== 'POST':
        fm=Add_Financial(request.POST)
        if fm.is_valid():
            fm.save()
            fm=Add_Financial()
    else:
      fm=Add_Financial()
    return render(request, 'AddFinancial.html', {'form':fm})



def delete_datas(request, pk):
    if request.method=='POST':
        pt=Financial.objects.get(studentid=pk)
        pt.delete()
        return HttpResponseRedirect('/')

def delete_datai(request, pk):
    if request.method=='POST':
        pt=Result.objects.get(studentid=pk)
        pt.delete()
        return HttpResponseRedirect('/')


def delete_datal(request, pk):
    if request.method=='POST':
        pt=Financial.objects.get(coursecode=pk)
        pt.delete()
        return HttpResponseRedirect('/')

def delete_data(request, studentid):
    if request.method=='POST':
        pi=Academic.objects.get(pk=studentid)
        pi.delete()
        return HttpResponseRedirect('/')

def delete_biography(request, pk):
    if request.method=="POST":
        ps=Item1.objects.get(studentid=pk)
        ps.delete()
        return HttpResponseRedirect('/')



def delete_result(request, pk):
    if request.method=="POST":
        pf=Result.objects.get(studentid=pk)
        pf.delete()
        return HttpResponseRedirect('/')


def delete_student(request, pk):
    if request.method=="POST":
        pi=Item3.objects.get(studentid=pk)
        pi.delete()
        return HttpResponseRedirect('/')


def delete_datam(request, pk):
    if request.method=='POST':
        fn=Item.objects.get(bin=pk)
        fn.delete()
        return HttpResponseRedirect('/')




