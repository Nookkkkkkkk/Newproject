from django.shortcuts import render
from .forms import *
# Create your views here.
def AddCoop13(request):
    student = Students.objects.all()
    establishments = Establishments.objects.all()
    form = Coop13Form(request.POST or None)
    if  form.is_valid():
        form.save()
        form = Coop13Form()
    context = {  
                'student' : student,
                'establishment' : establishments,
                'form' :form,           
    }
    
    return render(request,'coop13.html',context)

def AddCoop11(request):
    student = Students.objects.all()
    establishments = Establishments.objects.all()
    form = Coop11Form(request.POST or None)
    if  form.is_valid():
        form.save()
        form = Coop11Form()
    context = {  
                'student' : student,
                'establishment' : establishments,
                'form' :form,           
    }
    
    return render(request,'coop11.html',context)

def AddCoop112(request):
    student = Students.objects.all()
    establishments = Establishments.objects.all()
    form = Coop112Form(request.POST or None)
    if  form.is_valid():
        form.save()
        form = Coop112Form()
    context = {  
                'student' : student,
                'establishment' : establishments,
                'form' :form,           
    }
    
    return render(request,'coop112.html',context)

def AddCoop20(request):
    student = Students.objects.all()
    establishments = Establishments.objects.all()
    form = Coop20Form(request.POST or None)
    if  form.is_valid():
        form.save()
        form = Coop20Form()
    context = {  
                'student' : student,
                'establishment' : establishments,
                'form' :form,           
    }
    return render(request,'coop20.html',context)

def AddCoop211(request):
    student = Students.objects.all()
    establishments = Establishments.objects.all()
    form = Coop211Form(request.POST or None)
    if  form.is_valid():
        form.save()
        form = Coop211Form()
    context = {  
                'student' : student,
                'establishment' : establishments,
                'form' :form,           
    }
    
    return render(request,'coop211.html',context)

def AddCoop212(request):
    student = Students.objects.all()
    establishments = Establishments.objects.all()
    form = Coop212Form(request.POST or None)
    if  form.is_valid():
        form.save()
        form = Coop212Form()
    context = {  
                'student' : student,
                'establishment' : establishments,
                'form' :form,           
    }
    
    return render(request,'coop212.html',context)

def AddCoop213(request):
    student = Students.objects.all()
    establishments = Establishments.objects.all()
    form = Coop213Form(request.POST or None)
    if  form.is_valid():
        form.save()
        form = Coop213Form()
    context = {  
                'student' : student,
                'establishment' : establishments,
                'form' :form,           
    }
    
    return render(request,'coop213.html',context)