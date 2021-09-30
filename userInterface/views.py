from django.shortcuts import render
from office.models import FinicialAnalyst, PerviousCompany, Rates , FinicialCompany
from office.filters import RatesFilter

# Create your views here.


def user_interface(request, pk):
    context = {
        "analyst": FinicialAnalyst.objects.get(pk=pk),
        "pervcompanies": PerviousCompany.objects.filter(analyst_id=pk),
        "rates": Rates.objects.filter(AnalayticName_id=pk)
    }
    return render(request, 'userInterface/analyst-profile.html', context=context)


def rate_user_detail(request, pk):
    context = {
        "rate": Rates.objects.get(pk=pk)
    }
    return render(request, 'userInterface/rate-profile.html', context=context)


def user_home(request):
    label = []
    data = []
    rates = Rates.objects.filter(Recommendation__exact=1)[:5]
    for rate in rates:
        label.append(rate.CompanyEntered.name)
        data.append(rate.FairValue)
    label1 = []
    data1 = []
    rates = Rates.objects.filter(Recommendation__exact=2)[:5]
    for rate in rates:
        label1.append(rate.CompanyEntered.name)
        data1.append(rate.FairValue)
    companylabel = []
    companydata = []
    companies = Rates.objects.filter(Recommendation__exact=3)[:5]
    for company in companies:
        companylabel.append(company.CompanyEntered.name)
        data1.append(company.FairValue)
    rates = Rates.objects.all()[:10]
    rate_filter = RatesFilter(request.GET, queryset=rates)
    rate = rate_filter.qs
    context = {
        "myfilter": rate_filter,
        "rates": rate,
        "label": label,
        "data": data,
        "data1": data1,
        "label1": label1,
        "companylabel": companylabel,
        "companydata": companydata
    }
    return render(request, 'userInterface/home-page.html', context=context)


def analystslist(request):
    context = {
        "analysts": FinicialAnalyst.objects.all(),
    }
    return render(request, 'userInterface/analyst-list.html', context=context)


def PervList(request, pk):
    pervcopmainies = PerviousCompany.objects.filter(analyst_id=pk)
    analyst = FinicialAnalyst.objects.get(pk=pk)
    return render(request, 'userInterface/perlist.html', context={"companies": pervcopmainies, 'analyst': analyst})


def rateslist(request):
    context = {
        "rates": Rates.objects.all(),
    }
    return render(request, 'userInterface/rate-list.html', context=context)
