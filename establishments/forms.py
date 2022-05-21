from django import forms
from .models import *

class AddEstabForm(forms.ModelForm):
    class Meta:
        model = Establishments
        fields = '__all__'
        labels = {
        'name': 'ชื่อสถานประกอบการ',
        'address': 'ที่อยู่',
        'canton' : 'ตำบล',
        'district':'อำเภอ ',
        'province':'จังหวัด',
        'postcode':'รหัสไปรษณีย์ ',
        'email':'อีเมล์ ',
        'telephone':'โทรศัพท์ ',
    }