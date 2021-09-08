from django.shortcuts import render
from office.models import FinicialAnalyst, PerviousCompany, Rates


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
