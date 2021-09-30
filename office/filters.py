import django_filters
from django import forms

from .models import *


class RatesFilter(django_filters.FilterSet):
    code = django_filters.ModelChoiceFilter(field_name='CompanyEntered__code__code',
                                            queryset=CompanyCode.objects.all(),
                                            widget=forms.SelectMultiple(attrs={'class': "form-control"}))
    category = django_filters.ModelChoiceFilter(field_name='CompanyEntered__category',
                                                queryset=CompanyCategory.objects.all(),
                                                widget=forms.SelectMultiple(attrs={'class': "form-control"}))
    CompanyEntered = django_filters.ModelChoiceFilter(field_name='CompanyEntered',
                                                      queryset=FinicialCompany.objects.all(),
                                                      widget=forms.SelectMultiple(
                                                          attrs={'class': "form-control"}))
    name = django_filters.ModelChoiceFilter(field_name='AnalayticName', queryset=FinicialAnalyst.objects.all(),
                                            widget=forms.SelectMultiple(attrs={'class': "form-control"}))

    class Meta:
        model = Rates
        fields = ['CompanyEntered', 'category', 'code', 'name']
