from django.urls import path
from . import views

urlpatterns = [
   path('addstudent', views.AddStuent, name='addstudent'),
   path('search', views.search, name='search'),

]