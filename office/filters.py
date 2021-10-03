import django_filters

from .models import *


class RatesFilter(django_filters.FilterSet):
    company = django_filters.CharFilter(field_name='CompanyEntered__name', lookup_expr='icontains')
    date_of_rate = django_filters.DateFilter(field_name='RecommendDate', lookup_expr='gt', )
    end_of_rate = django_filters.DateFilter(field_name='RecommendDate', lookup_expr='lt', )
    analyst = django_filters.CharFilter(field_name='AnalayticName__name', lookup_expr='icontains')
    code = django_filters.CharFilter(field_name='CompanyEntered__company__code', lookup_expr='icontains')

    class Meta:
        model = Rates
        fields = ['company', 'date_of_rate', 'analyst', 'code', 'end_of_rate']
