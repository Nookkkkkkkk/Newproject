from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .forms import LoginForm, RegistersForm
from django.contrib.auth import login, logout


# Create your views here.
def RegisterAccounts(request):
    form = RegistersForm(request.POST or None)
    if  form.is_valid():
        form.save()
        form = RegistersForm()
    context = {  
                'form' :form,           
    }
    return render(request,'register.html',context)



