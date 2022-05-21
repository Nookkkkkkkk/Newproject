from django.shortcuts import render
from .models import Students
from .filters import StudentFilter
from .forms import *
# Create your views here.

def AddStuent(request):
    form = AddStudentForm(request.POST or None)
    if  form.is_valid():
        form.save()
        form = AddStudentForm()
    context = {            
                'form' :form,           
    }
    return render(request,'addstudent.html',context)

def search(request):
    user_list = Students.objects.all()
    user_filter = StudentFilter(request.GET, queryset=user_list)
    return render(request, 'user_list.html', {'filter': user_filter})