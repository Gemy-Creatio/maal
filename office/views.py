from datetime import datetime

from django.http import HttpResponse

from maal.utils import render_to_pdf
from django.template.loader import get_template
from django.views import View
from accounts.models import User
from django.shortcuts import render, redirect
from .models import Rates, FinicialCompany, FinicialAnalyst, CompanyCode
from django.core.files.storage import FileSystemStorage


def RatesList(request):
    rates = Rates.objects.all()
    return render(request, 'office/rates-list.html', context={"rates": rates})


def AnalystsList(request):
    analayts = FinicialAnalyst.objects.all()
    return render(request, 'office/analysts-list.html', context={"analayts": analayts})


def AddAnalyst(request):
    company = FinicialCompany.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        currentCompany = request.POST.get('currentCompany')
        currentJob = request.POST.get('currentJob')
        pervCompany = request.POST.get('pervCompany')
        pervJob = request.POST.get('pervJob')
        phone = int(request.POST.get('phone'))
        email = request.POST.get('email')
        twitterAccount = request.POST.get('twitterAccount')

        analyst = FinicialAnalyst(name=name, phone=phone, tiwtterAccount=twitterAccount, email=email,
                                  currentCompany_id=currentCompany, currentJob=currentJob,
                                  pervCompany_id=pervCompany, pervJob=pervJob)
        analyst.save()
        if analyst.pk:
            return redirect('analyst-list')
        else:
            return render(request, 'office/add-analyst.html', context={"companies": company})
    return render(request, 'office/add-analyst.html', context={"companies": company})


def AddRate(request):
    company = FinicialCompany.objects.all()
    analyst = FinicialAnalyst.objects.all()
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
        rate = Rates(CompanyEntered_id=CompanyEntered, EmpEntered_id=request.user.pk, Recommendation=Recommendation,
                     ResearchCompany_id=ResearchCompany, AnalayticName_id=AnalayticName, report=report,
                     CurrenncyValue=float(CurrenncyValue), MarketValue=float(MarketValue), FairValue=float(FairValue))
        rate.save()
        if rate.pk:
            return redirect('rates-list')
        else:
            return render(request, 'office/add-rate.html', context={"companies": company, "analysts": analyst})
    return render(request, 'office/add-rate.html', context={"companies": company, "analysts": analyst})


def UpdateAnalyst(request, pk):
    analyst = FinicialAnalyst.objects.get(pk=pk)
    company = FinicialCompany.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        currentCompany = request.POST.get('currentCompany')
        currentJob = request.POST.get('currentJob')
        pervCompany = request.POST.get('pervCompany')
        pervJob = request.POST.get('pervJob')
        phone = int(request.POST.get('phone'))
        email = request.POST.get('email')
        twitterAccount = request.POST.get('twitterAccount')
        analyst.name = name
        analyst.currentCompany_id = currentCompany
        analyst.CurrentJob = currentJob
        analyst.pervJob = pervJob
        analyst.pervCompany_id = pervCompany
        analyst.phone = phone
        analyst.email = email
        analyst.tiwtterAccount = twitterAccount
        if analyst.pk:
            return redirect('analyst-list')
        else:
            return render(request, 'office/update-analyst.html')
    return render(request, 'office/update-analyst.html', context={"analyst": analyst, "companies": company})


def UpdateRate(request, pk):
    rate = Rates.objects.get(pk=pk)
    company = FinicialCompany.objects.all()
    analyst = FinicialAnalyst.objects.all()
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
        rate.CompanyEntered_id = CompanyEntered.pk
        rate.report = report
        rate.AnalayticName_id = AnalayticName.pk
        rate.FairValue = float(FairValue)
        rate.MarketValue = float(MarketValue)
        rate.CurrenncyValue = float(CurrenncyValue)
        rate.Recommendation = Recommendation
        rate.ResearchCompany_id = ResearchCompany.pk
        rate.EmpEntered_id = request.user.pk
        rate.save()
        if rate.pk:
            return redirect('rate-list')
        else:
            return render(request, 'office/update-rate.html')
    return render(request, 'office/update-rate.html', context={"rate": rate, "companies": company, "analysts": analyst})


def RateDetails(request, pk):
    rate = Rates.objects.get(pk=pk)
    return render(request, 'office/rate-detail.html', context={"rate": rate})


def AnalystDetails(request, pk):
    analyst = FinicialAnalyst.objects.get(pk=pk)
    return render(request, 'office/analyst-detail.html', context={"analyst": analyst})


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



class AnalystsAllReport(View):
    def get(self, request, *args, **kwargs):
        template = get_template('analysts-all-pdf.html')
        analayts = FinicialAnalyst.objects.all()
        user_obj = User.objects.get(pk=request.user.pk)
        context = {
            "company": "صحفية مال الأقتصادية ",
            "user": user_obj,
            "analayts": analayts,
            "topic": "المحللين المالين",
            "today": datetime.today().strftime('%Y-%m-%d'),
        }
        html = template.render(context)
        pdf = render_to_pdf('analysts-all-pdf.html', context)
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
