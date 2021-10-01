import django_filters

from .models import *


class RatesFilter(django_filters.FilterSet):
    company = django_filters.CharFilter(field_name='CompanyEntered__name', lookup_expr='iexact')
    date_of_rate = django_filters.DateFilter(field_name='RecommendDate', lookup_expr='exact')
    analyst = django_filters.CharFilter(field_name='AnalayticName__name', lookup_expr='iexact')
    code = django_filters.CharFilter(field_name='CompanyEntered__company__code', lookup_expr='iexact')

    class Meta:
        model = Rates
        fields = ['company', 'date_of_rate', 'analyst', 'code']
