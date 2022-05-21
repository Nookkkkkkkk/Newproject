from lib2to3.pgen2.token import NAME
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from students.models import Students
from establishments.models import Establishments
from django.core.paginator import Paginator
from django.contrib.auth import login, logout
from django.db.models import Q
# Create your views here.

def index(request):
    return render(request,'index.html')

def download(request):
    return render(request,'download.html')

def liststudent(request):
    student = Students.objects.all()
    student_paginator = Paginator(student,12)
    page_num = request.GET.get('page')
    page = student_paginator.get_page(page_num)
    context = {
        'count' :  student_paginator.count,
        'page' : page
    }
    return render(request,'student.html',context)

def listestab(request):
    estab = Establishments.objects.all()
    estab_paginator = Paginator(estab,12)
    page_num = request.GET.get('page')
    page = estab_paginator.get_page(page_num)
    context = {
        'count' : estab_paginator.count,
        'page' : page
    }
    return render(request,'estab.html',context)

def login(request):
    username=request.POST['username']
    password=request.POST['password']
    #login เช็ค user กับ pass
    userlogin=auth.authenticate(username=username,password=password) 
    if userlogin is not None :
        auth.login(request,userlogin)
        return redirect('/home')
    else :
        messages.info(request,'ไม่พบข้อมูล')
        return redirect('/')  
def logout(request):
    auth.logout(request)
    return redirect('/')

def home(request):
    student = Students.objects.all()
    estab = Establishments.objects.all()
    context = {
            'Students' : student,
            'Establishments' : estab ,

    }
    return render(request,'home.html',context)


def searchstudent(request):
    search_post = request.GET.get('q')
    if search_post:
        print(search_post)
        students = Students.objects.filter(Q(STUDENT_NO__icontains=search_post))
    else:
        print("Empty")
        return redirect("/")
    return render(request, 'searchstudent.html',{'students': students})


def searchestab(request):
    search_post = request.GET.get('q')
    if search_post:
        print(search_post)
        estab = Establishments.objects.filter(Q(name__icontains=search_post))
    else:
        print("Empty")
        return redirect("/")
    return render(request, 'searchestab.html',{'estab': estab})

def adddata(request):
    return render(request,'adddata.html',)