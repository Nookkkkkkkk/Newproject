from django import forms
from .models import Accounts


class RegistersForm(forms.ModelForm):
    class Meta:
        model = Accounts
        fields = "__all__"
        widgets = {
            'password': forms.PasswordInput(render_value=True)
        }

class LoginForm(forms.ModelForm):
    class Meta:
        model = Accounts
        exclude = 'prefix','name','lastname','status'
        widgets = {
            'password': forms.PasswordInput(render_value=True)
        }

