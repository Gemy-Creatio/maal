from django import forms
from . import models


class SeniorOwnerForm(forms.ModelForm):
    class Meta:
        model = models.SeniorOwner
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(
                attrs={'id': 'namefield', 'class': 'form-control', 'placeholder': 'إسم المالك '}),
            'description': forms.TextInput(
                attrs={'id': 'descriptionfield', 'class': 'form-control', 'placeholder': 'نبذه عته '}),
        }


class ArrowsForm(forms.ModelForm):
    class Meta:
        model = models.CompaniesArrow
        fields = ['company', 'owner', 'numberOFArrows']
        widgets = {
            'owner': forms.Select(choices=models.SeniorOwner.objects.all()),
            'numberOFArrows': forms.NumberInput(
                attrs={'id': 'numberOFArrowsfield', 'class': 'form-control', 'placeholder': 'عدد الأسهم'}),
           
            'company': forms.Select(choices=models.FinicialCompany.objects.all())
        }

class ClientForm(forms.ModelForm):
    class Meta:
        model = models.Client
        fields = ['name', 'phone', 'email']
        labels = {
            'name' : 'الأسم' , 
            'phone' : 'الهاتف' , 
            'email' : 'البريد الألكترونى' , 
        }
        widgets = {
            'name': forms.TextInput(
                attrs={'id': 'namefield', 'class': 'form-control', 'placeholder': 'الأسم'}),
            'phone': forms.NumberInput(
                attrs={'id': 'phonefield', 'class': 'form-control', 'placeholder': 'الهاتف'}),
           
            'email': forms.TextInput(
                attrs={'id': 'emailfield', 'class': 'form-control', 'placeholder': 'البريد الألكترونى'}),
        }