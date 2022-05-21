from django.shortcuts import render
from .models import Establishments
from .forms import *
from .filters import EstablishmentsFilter

# Create your views here.
def AddEstab(request):
    form = AddEstabForm(request.POST or None)
    if  form.is_valid():
        form.save()
        form = AddEstabForm()
    context = {            
                'form' :form,           
    }
    return render(request,'adddata.html',context)

def search(request):
    user_list = Establishments.objects.all()
    user_filter = EstablishmentsFilter(request.GET, queryset=user_list)
    return render(request, 'estab_list.html', {'filter': user_filter})