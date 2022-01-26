from django import forms
from office import models


class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.CompanyCategory
        fields = '__all__'
        exclude = ['EmpEntered']
        labels = {
            'name': 'اسم القطاع'
        }


class ResearchCompanyForm(forms.ModelForm):
    class Meta:
        model = models.ResearchCompany
        fields = '__all__'
        exclude = ['EmpEntered']
        labels = {
            'name': 'اسم الشركة'
        }


class CompanyCodeForm(forms.ModelForm):
    class Meta:
        model = models.CompanyCode
        fields = '__all__'
        labels = {
            'code' : 'كود الشركة',
            'company' : 'إختر الشركة'
        }
