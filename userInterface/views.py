from django.shortcuts import render
from django.views.generic import ListView

from office.models import FinicialAnalyst, CompanyCategory, PerviousCompany, Rates, FinicialCompany, EarningsForecast, \
    ResearchCompany
from office.filters import RatesFilter, EarnFilter
from owners.models import CompaniesArrow, SeniorOwner, FinicalCompaniesArrow
from wishlist.models import Wishlist
from django.core.paginator import Paginator
from main.models import (
EarningHeader
)

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
    arrows = SeniorOwner.objects.all()[:5]
    max_date = CompaniesArrow.objects.latest('date').date
    arrows = CompaniesArrow.objects.filter(date=max_date)
    label = []
    data = []
    rates = Rates.objects.filter(Recommendation=1)[:5]
    for rate in rates:
        label.append(rate.CompanyEntered.name)
        data.append(rate.FairValue)
    label1 = []
    data1 = []
    rates = Rates.objects.filter(Recommendation=2)[:5]
    for rate in rates:
        label1.append(rate.CompanyEntered.name)
        data1.append(rate.FairValue)
    companylabel = []
    companydata = []
    companies = Rates.objects.filter(Recommendation=3)[:5]
    for company in companies:
        companylabel.append(company.CompanyEntered.name)
        companydata.append(company.FairValue)
    companies = FinicialCompany.objects.order_by('CompanyEntered')[:5]
    companylabel1 = []
    companydata1 = []
    for company in companies:
        companylabel1.append(company.name)
        companydata1.append(company.CompanyEntered.count())
    rates = Rates.objects.filter(is_recommended=True)
    rate_filter = RatesFilter(request.POST, queryset=rates)
    rate = rate_filter.qs[:10]
    context = {
        "cats": cats,
        "comps": comps,
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
        "arrows": arrows,
        "companyarrows": arrows,
        "last_date":max_date,
    }
    return render(request, 'userInterface/home-page.html', context=context)


def analystslist(request):
    analyts = FinicialAnalyst.objects.all()
    paginator = Paginator(analyts, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "analysts": page_obj,
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
    paginator = Paginator(rate, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "myfilter": rate_filter,
        "rates": page_obj,
    }
    return render(request, 'userInterface/rate-list.html', context=context)


def expectList(request):
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
    content = EarningHeader.get_solo()
    for expect in data1:
        expectlabel1.append(expect.CompanyEntered.name)
        expectdata1.append(expect.total_earn)
    expects = EarningsForecast.objects.filter(is_recommended=True)
    expect_filter = EarnFilter(request.POST, queryset=expects)
    expectz = expect_filter.qs
    paginator = Paginator(expectz, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "expects": page_obj,
        "myfilter": expect_filter,
        "expectlabel": expectlabel,
        "expectdata": expectdata,
        "expectlabel1": expectlabel1,
        "expectdata1": expectdata1,
        "expectlabel2": expectlabel2,
        "expectdata2": expectdata2,
        "expectlabel3": expectlabel3,
        "expectdata3": expectdata3,
        "content":content,
    }
    return render(request, 'userInterface/expect-list.html', context=context)


def CompanyArrowsAll(request):
    object_list = FinicalCompaniesArrow.objects.all()
    paginator = Paginator(object_list, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # data = FinicalCompaniesArrow.objects.filter('-ownRatio')
    # expectlabel = []
    # expectdata = []
    # for arrow in data:
    #     expectlabel.append(arrow.company.name)
    #     expectdata.append(arrow.ownRatio)
    # data1 = FinicalCompaniesArrow.objects.filter('-arrowPrice')
    # expectlabel1 = []
    # expectdata1 = []
    # for arrow in data1:
    #     expectlabel1.append(arrow.company.name)
    #     expectdata1.append(arrow.arrowPrice)
    context = {
        "object_list": page_obj,
    }
    return render(request, 'userInterface/companiesArrowsownerList.html', context=context)


def ExpectAll(request):
    object_list = EarningsForecast.objects.all()
    paginator = Paginator(object_list, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "object_list": page_obj,
    }
    return render(request, 'userInterface/all_expectation.html', context=context)


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
    paginator = Paginator(expectz, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "expects": page_obj,
        "myfilter": expect_filter,
        "expectlabel": expectlabel,
        "expectdata": expectdata,
        "expectlabel1": expectlabel1,
        "expectdata1": expectdata1,
        "expectlabel2": expectlabel2,
        "expectdata2": expectdata2,
        "expectlabel3": expectlabel3,
        "expectdata3": expectdata3,
        "content": EarningHeader.get_solo()

    }
    return render(request, 'userInterface/expectreal-list.html', context=context)


def CapitalProfile(request, pk):
    data = FinicialCompany.objects.get(pk=pk)
    arrows = CompaniesArrow.objects.filter(company__id=pk)
    return render(request, 'userInterface/capital-profile.html', context={"data": data, "arrows": arrows})


def ResearchProfile(request, pk):
    data = ResearchCompany.objects.get(pk=pk)
    return render(request, 'userInterface/researchProfile.html', context={"data": data})
