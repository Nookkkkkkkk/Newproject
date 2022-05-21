from django.urls import path
from . import views

urlpatterns = [
    path('adddata',views.AddEstab,name ='adddata'),
    path('es',views.search,name ='es'),
]