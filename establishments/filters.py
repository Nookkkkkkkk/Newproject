from .models import *
import django_filters

class EstablishmentsFilter(django_filters.FilterSet):
    class Meta:
        model = Establishments
        fields = ['name', ]
        