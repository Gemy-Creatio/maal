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
        fields = ['company', 'owner', 'total_arrows_owned', 'ownRatio', 'totalOwnRatioToday',
                  'totalOwnRatioYesterday']
        widgets = {
            'owner': forms.Select(choices=models.SeniorOwner.objects.all()),
            'total_arrows_owned': forms.NumberInput(
                attrs={'id': 'numberOFArrowsfield', 'class': 'form-control', 'placeholder': 'عدد الأسهم'}),
            'totalOwnRatioYesterday': forms.NumberInput(
                attrs={'id': 'totalOwnRatioYesterday', 'class': 'form-control', 'placeholder': 'إجمالى نسبة الملكية اليوم السابق'}),
            'totalOwnRatioToday': forms.NumberInput(
                attrs={'id': 'totalOwnRatioToday', 'class': 'form-control', 'placeholder': 'إجمالى نسبة الملكية اليوم '}),
            'ownRatio': forms.NumberInput(
                attrs={'id': 'arrowPricefield', 'class': 'form-control', 'placeholder': 'نسبة الملكية'}),
            'company': forms.Select(choices=models.FinicialCompany.objects.all())
        }


class CompaniesArrowsForm(forms.ModelForm):
    class Meta:
        model = models.FinicalCompaniesArrow
        fields = ['company', 'owner', 'numberOFArrows', 'ownRatio']
        widgets = {
            'owner': forms.Select(choices=models.FinicialCompany.objects.all()),
            'numberOFArrows': forms.NumberInput(
                attrs={'id': 'numberOFArrowsfield', 'class': 'form-control', 'placeholder': 'عدد الأسهم'}),
            'ownRatio': forms.NumberInput(
                attrs={'id': 'arrowPricefield', 'class': 'form-control', 'placeholder': 'نسبة الملكية'}),
            'company': forms.Select(choices=models.FinicialCompany.objects.all())
        }
        labels = {
            'company': 'الشركة المالكة',
            'owner': 'الشركة المملوكة',
            'numberOFArrows': 'عدد الأسهم',
            'ownRatio': 'نسبة الملكية',

        }
