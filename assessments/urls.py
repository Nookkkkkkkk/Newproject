from django.urls import path
from . import views

urlpatterns = [
    path('coop13', views.AddCoop13, name='coop13'),
    path('coop11', views.AddCoop11, name='coop11'),
    path('coop11-2', views.AddCoop112, name='coop11-2'),
    path('coop20', views.AddCoop20, name='coop20'),
    path('coop21-1', views.AddCoop211, name='coop21-1'),
    path('coop21-2', views.AddCoop212, name='coop21-2'),
    path('coop21-3', views.AddCoop213, name='coop21-3'),
    
    
]