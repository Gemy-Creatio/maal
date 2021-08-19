from datetime import datetime

from django.http import HttpResponse

from maal.utils import render_to_pdf
from django.template.loader import get_template
from django.views import View
from accounts.models import User
from django.shortcuts import render, redirect
from .models import Rates
from django.core.files.storage import FileSystemStorage


def RatesList(request):
    rates = Rates.objects.all()
    return render(request, 'office/rates-list.html', context={"rates": rates})


def AddRate(request):
    if request.method == 'POST' and request.FILES['report']:
        CompanyEntered = request.POST.get('CompanyEntered')
        report = request.FILES['report']
        fs = FileSystemStorage()
        filename = fs.save(report.name, report)
        ResearchCompany = request.POST.get('ResearchCompany')
        AnalayticName = request.POST.get('AnalayticName')
        Recommendation = request.POST.get('Recommendation')
        CurrenncyValue = request.POST.get('CurrenncyValue')
        FairValue = request.POST.get('FairValue')
        MarketValue = request.POST.get('MarketValue')
        rate = Rates(CompanyEntered=CompanyEntered, EmpEntered_id=request.user.pk, Recommendation=Recommendation,
                     ResearchCompany=ResearchCompany, AnalayticName=AnalayticName, report=report,
                     CurrenncyValue=float(CurrenncyValue), MarketValue=float(MarketValue), FairValue=float(FairValue))
        rate.save()
        if rate.pk:
            return redirect('rates-list')
        else:
            return render(request, 'office/add-rate.html')
    return render(request, 'office/add-rate.html')


def UpdateRate(request, pk):
    rate = Rates.objects.get(pk=pk)
    if request.method == 'POST' and request.FILES['report']:
        CompanyEntered = request.POST.get('CompanyEntered')
        report = request.FILES['report']
        fs = FileSystemStorage()
        filename = fs.save(report.name, report)
        ResearchCompany = request.POST.get('ResearchCompany')
        AnalayticName = request.POST.get('AnalayticName')
        Recommendation = request.POST.get('Recommendation')
        CurrenncyValue = request.POST.get('CurrenncyValue')
        FairValue = request.POST.get('FairValue')
        MarketValue = request.POST.get('MarketValue')
        rate.CompanyEntered = CompanyEntered
        rate.report = report
        rate.AnalayticName = AnalayticName
        rate.FairValue = float(FairValue)
        rate.MarketValue = float(MarketValue)
        rate.CurrenncyValue = float(CurrenncyValue)
        rate.Recommendation = Recommendation
        rate.ResearchCompany = ResearchCompany
        rate.save()
        if rate.pk:
            return redirect('rate-list')
        else:
            return render(request, 'office/update-rate.html')
    return render(request, 'office/update-rate.html', context={"rate": rate})


def RateDetails(request, pk):
    rate = Rates.objects.get(pk=pk)
    return render(request, 'office/rate-detail.html', context={"rate": rate})



class RatesAllReport(View):
    def get(self, request, *args, **kwargs):
        template = get_template('rates-all-pdf.html')
        rates = Rates.objects.all()
        user_obj = User.objects.get(pk=request.user.pk)
        context = {
            "company": "صحفية مال الأقتصادية ",
            "user": user_obj,
            "rates": rates,
            "topic": "التقييمات البحثية",
            "today": datetime.today().strftime('%Y-%m-%d'),
        }
        html = template.render(context)
        pdf = render_to_pdf('rates-all-pdf.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" % ("12341231")
            content = "inline; filename='%s'" % (filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" % (filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")