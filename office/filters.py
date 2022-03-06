import django_filters

from .models import *


class YearFilter(django_filters.FilterSet):
    real_earn = django_filters.NumberFilter(field_name='real_earn')
    expect_earn = django_filters.NumberFilter(field_name='expect_earn')
    quarter_now = django_filters.NumberFilter(field_name='quarter_now')
    quarter_past = django_filters.NumberFilter(field_name='quarter_past')

    class Meta:
        model = ExpectationYear
        fields = ['real_earn', 'expect_earn', 'quarter_now', 'quarter_past']


class RatesFilter(django_filters.FilterSet):
    company = django_filters.CharFilter(field_name='CompanyEntered__name', lookup_expr='icontains')
    date_of_rate = django_filters.DateFilter(field_name='RecommendDate', lookup_expr='gt', )
    end_of_rate = django_filters.DateFilter(field_name='RecommendDate', lookup_expr='lt', )
    analyst = django_filters.CharFilter(field_name='AnalayticName__name', lookup_expr='icontains')
    code = django_filters.CharFilter(field_name='CompanyEntered__company__code', lookup_expr='icontains')

    class Meta:
        model = Rates
        fields = ['company', 'date_of_rate', 'analyst', 'code', 'end_of_rate']


class EarnFilter(django_filters.FilterSet):
    company = django_filters.CharFilter(field_name='CompanyEntered__name', lookup_expr='icontains')
    analyst = django_filters.CharFilter(field_name='analyst__name', lookup_expr='icontains')
    code = django_filters.CharFilter(field_name='CompanyEntered__company__code', lookup_expr='icontains')

    class Meta:
        model = EarningsForecast
        fields = ['company', 'analyst', 'code']
