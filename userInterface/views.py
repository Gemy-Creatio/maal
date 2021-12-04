from django.shortcuts import render
from office.models import FinicialAnalyst,CompanyCategory, PerviousCompany, Rates, FinicialCompany, EarningsForecast, ResearchCompany
from office.filters import RatesFilter, EarnFilter
from owners.models import CompaniesArrow
from wishlist.models import Wishlist
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
    cats = CompanyCategory.objects.all()
    comps = FinicialCompany.objects.all()
    arrows = CompaniesArrow.objects.order_by('-numberOFArrows')
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
        companydata.append(company.FairValue)
    companies = FinicialCompany.objects.order_by('CompanyEntered')[:5]
    companylabel1 = []
    companydata1 = []
    for company in companies:
        companylabel1.append(company.name)
        companydata1.append(company.CompanyEntered.count())
    rates = Rates.objects.all()
    rate_filter = RatesFilter(request.POST, queryset=rates)
    rate = rate_filter.qs[:10]
    context = {
         "cats":cats,
        "comps":comps,
        "myfilter": rate_filter,
        "rates": rate,
        "label": label,
        "data": data,
        "data1": data1,
        "label1": label1,
        "companylabel": companylabel,
        "companydata": companydata,
        "companylabel1": companylabel1,
        "companydata1": companydata1,
        "arrows":arrows
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
    rates = Rates.objects.all()
    rate_filter = RatesFilter(request.GET, queryset=rates)
    rate = rate_filter.qs
    context = {
        "myfilter": rate_filter,
        "rates": rate,
    }
    return render(request, 'userInterface/rate-list.html', context=context)


def expectList(request):
    expects = EarningsForecast.objects.all()
    data = EarningsForecast.objects.order_by('-realEarn')[:5]
    expectlabel = []
    expectdata = []
    for expect in data:
        expectlabel.append(expect.CompanyEntered.name)
        expectdata.append(expect.realEarn)
    data2 = EarningsForecast.objects.order_by('-third2020')[:5]
    expectlabel2 = []
    expectdata2 = []
    for expect in data2:
        expectlabel2.append(expect.CompanyEntered.name)
        expectdata2.append(expect.third2020)
    data3 = EarningsForecast.objects.order_by('-second2020')[:5]
    expectlabel3 = []
    expectdata3 = []
    for expect in data3:
        expectlabel3.append(expect.CompanyEntered.name)
        expectdata3.append(expect.second2020)
    data1 = EarningsForecast.objects.order_by('-total_earn')[:5]
    expectlabel1 = []
    expectdata1 = []
    for expect in data1:
        expectlabel1.append(expect.CompanyEntered.name)
        expectdata1.append(expect.total_earn)
    expectss = EarningsForecast.objects.all()
    expect_filter = EarnFilter(request.POST, queryset=expectss)
    expectz = expect_filter.qs
    
    context = {
        "expects": expectz,
        "myfilter": expect_filter,
        "expectlabel": expectlabel,
        "expectdata": expectdata,
        "expectlabel1": expectlabel1,
        "expectdata1": expectdata1,
        "expectlabel2": expectlabel2,
        "expectdata2": expectdata2,
        "expectlabel3": expectlabel3,
        "expectdata3": expectdata3

    }
    return render(request, 'userInterface/expect-list.html', context=context)


def expectrealList(request):
    expects = EarningsForecast.objects.all()
    data = EarningsForecast.objects.order_by('-realEarn')[:5]
    expectlabel = []
    expectdata = []
    for expect in data:
        expectlabel.append(expect.CompanyEntered.name)
        expectdata.append(expect.realEarn)
    data1 = EarningsForecast.objects.order_by('-total_earn')[:5]
    expectlabel1 = []
    expectdata1 = []
    for expect in data1:
        expectlabel1.append(expect.CompanyEntered.name)
        expectdata1.append(expect.total_earn)
    data2 = EarningsForecast.objects.order_by('-third2020')[:5]
    expectlabel2 = []
    expectdata2 = []
    for expect in data2:
        expectlabel2.append(expect.CompanyEntered.name)
        expectdata2.append(expect.third2020)
    data3 = EarningsForecast.objects.order_by('-second2020')[:5]
    expectlabel3 = []
    expectdata3 = []
    for expect in data3:
        expectlabel3.append(expect.CompanyEntered.name)
        expectdata3.append(expect.second2020)
    expectss = EarningsForecast.objects.all()
    expect_filter = EarnFilter(request.POST, queryset=expectss)
    expectz = expect_filter.qs
    context = {
        "expects": expectz,
        "myfilter": expect_filter,
        "expectlabel": expectlabel,
        "expectdata": expectdata,
        "expectlabel1": expectlabel1,
        "expectdata1": expectdata1,
        "expectlabel2": expectlabel2,
        "expectdata2": expectdata2,
        "expectlabel3": expectlabel3,
        "expectdata3": expectdata3

    }
    return render(request, 'userInterface/expectreal-list.html', context=context)


def CapitalProfile(request, pk):
    data = FinicialCompany.objects.get(pk=pk)
    arrows = CompaniesArrow.objects.filter(company__id = pk)
    return render(request, 'userInterface/capital-profile.html', context={"data": data , "arrows":arrows})


def ResearchProfile(request, pk):
    data = ResearchCompany.objects.get(pk=pk)
    return render(request, 'userInterface/researchProfile.html', context={"data": data})
