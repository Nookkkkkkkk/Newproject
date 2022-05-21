from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('home', views.home, name='home'),
    path('',views.index),
    path('login', views.login),
    path('logout',login_required(views.logout,login_url='/#login')),
    path('liststudent', views.liststudent,name='liststudent'),
    path('listestab', views.listestab,name='listestab'),
    path('download',views.download,name ='download'),
    path('searchstudent',views.searchstudent,name ='searchstudent'),
    path('searchestab',views.searchestab,name ='searchestab'),
    

]