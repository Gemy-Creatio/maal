from django import forms
from .models import User
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name']
        widgets = {
            'password': forms.PasswordInput(attrs={'id': 'passwordfield', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'id': 'emailfield', 'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'id': 'firstnamefield', 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'id': 'lastnamefield', 'class': 'form-control'}),

        }