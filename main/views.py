import datetime

from django.shortcuts import render
from office.models import FinicialAnalyst, FinicialCompany, Rates, User, ResearchCompany, EarningsForecast


def home_page(request):
    context = {
        "rate_count": Rates.objects.all().count(),
        "analysts_count": FinicialAnalyst.objects.all().count(),
        "companies_count": FinicialCompany.objects.all().count(),
        "emp_count": User.objects.filter(user_type=2).count()
    }
    return render(request, 'main/home.html', context=context)


def reports_page(request):
    return render(request, 'main/reports.html')


def user_page(request):
    return render(request, 'main/user-home.html')


def master_home(request):
    labels = []
    data = []
    Ratelabels = []
    RateData = []
    Companieslabels = []
    CompaniesData = []
    # expectlabels = []
    # expectData = []
    # expects = EarningsForecast.objects.order_by('analyst')[:5]
    # for expect in expects:
    #     expectlabels.append(expect.ResearchCompany.name)
    #     expectData.append(expect.expectyear_set.all().)

    companies = FinicialCompany.objects.order_by('CompanyEntered')[:5]
    for company in companies:
        Companieslabels.append(company.name)
        CompaniesData.append(company.CompanyEntered.count())
    rates = Rates.objects.order_by('-MarketValue')[:5]
    for rate in rates:
        Ratelabels.append(rate.ResearchCompany.name)
        RateData.append(rate.MarketValue)
    queryset = FinicialAnalyst.objects.order_by('-AnalayticName')[:5]
    for analyst in queryset:
        labels.append(analyst.name)
        data.append(analyst.AnalayticName.count())
    context = {
        "high_rated": Rates.objects.all().order_by('-RecommendDate')[:10],
        "analysts": FinicialAnalyst.objects.all().order_by('-name')[:10],
        "today": datetime.datetime.now().date(),
        "rates_count": Rates.objects.count(),
        "analysts__count": FinicialAnalyst.objects.count(),
        "companies_count": FinicialCompany.objects.count(),
        'labels': labels,
        'data': data,
        'RateLables': Ratelabels,
        'RateData': RateData,
        'companiesLables': Companieslabels,
        'companiesData': CompaniesData,
        # 'expectlables': expectlabels,
        # 'expectData': expectData,
        "expectations": EarningsForecast.objects.all()[:5]
    }
    return render(request, 'main/master_home.html', context=context)
