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

