from datetime import datetime

from django.http import HttpResponse

from maal.utils import render_to_pdf
from django.template.loader import get_template
from django.views import View
from accounts.models import User
from django.shortcuts import render, redirect
from .models import Rates, FinicialCompany, FinicialAnalyst, CompanyCode, CompanyCategory, ResearchCompany
from django.core.files.storage import FileSystemStorage


def RatesList(request):
    rates = Rates.objects.all()
    return render(request, 'office/rates-list.html', context={"rates": rates})


def Research_List(request):
    companies = ResearchCompany.objects.all()
    return render(request, 'office/research_list.html', context={"companies": companies})


def Company_List(request):
    companies = FinicialCompany.objects.all()
    return render(request, 'office/company_list.html', context={"companies": companies})


def Category_List(request):
    category = CompanyCategory.objects.all()
    return render(request, 'office/catgory-list.html', context={"categories": category})


def AddCategory(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        category = CompanyCategory(name=name, EmpEntered_id=request.user.pk)
        category.save()
        if category.pk:
            return redirect('category-list')
        else:
            return render(request, 'office/add-category.html')
    return render(request, 'office/add-category.html')


def AddResearch(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        company = ResearchCompany(name=name, EmpEntered_id=request.user.pk)
        company.save()
        if company.pk:
            return redirect('research-list')
        else:
            return render(request, 'office/add-research.html')
    return render(request, 'office/add-research.html')


def AddCompany(request):
    categories = CompanyCategory.objects.all()
    context = {"categories": categories}
    if request.method == 'POST':
        name = request.POST.get('name')
        category = request.POST.get('category')
        company = FinicialCompany(name=name, EmpEntered_id=request.user.pk, category_id=category)
        company.save()
        if company.pk:
            return redirect('company-list')
        else:
            return render(request, 'office/add-company.html', context=context)
    return render(request, 'office/add-company.html', context=context)


def EditCompany(request, pk):
    company = FinicialCompany.objects.get(pk=pk)
    categories = CompanyCategory.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        category = request.POST.get('category')
        company.name = name
        company.category_id = category
        company.EmpEntered_id = request.user.pk
        company.save()
        if company.pk:
            return redirect('company-list')
        else:
            return render(request, 'office/edit-company.html', context={"company": company, "categories": categories})
    return render(request, 'office/edit-company.html', context={"company": company, "categories": categories})


def EditCategory(request, pk):
    catgeory = CompanyCategory.objects.get(pk=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        category_id = request.POST.get('category')
        catgeory.name = name
        catgeory.category_id = category_id
        catgeory.EmpEntered_id = request.user.pk
        catgeory.save()
        if catgeory.pk:
            return redirect('category-list')
        else:
            return render(request, 'office/edit-category.html', context={"category": catgeory})
    return render(request, 'office/edit-category.html', context={"category": catgeory})


def EditResearch(request, pk):
    company = ResearchCompany.objects.get(pk=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        company.name = name
        company.EmpEntered_id = request.user.pk
        company.save()
        if company.pk:
            return redirect('research-list')
        else:
            return render(request, 'office/edit-research.html', context={"company": company})
    return render(request, 'office/edit-research.html', context={"company": company})


def AnalystsList(request):
    analayts = FinicialAnalyst.objects.all()
    return render(request, 'office/analysts-list.html', context={"analayts": analayts})


def AddAnalyst(request):
    company = FinicialCompany.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        currentCompany = request.POST.get('currentCompany')
        currentJob = request.POST.get('currentJob')
        pervCompany = request.POST.getlist('pervCompany')
        pervJob = request.POST.get('pervJob')
        phone = int(request.POST.get('phone'))
        email = request.POST.get('email')
        twitterAccount = request.POST.get('twitterAccount')

        analyst = FinicialAnalyst.objects.create(name=name, phone=phone, tiwtterAccount=twitterAccount, email=email,
                                                 currentCompany_id=currentCompany, CurrentJob=currentJob,
                                                 pervJob=pervJob)
        companies = FinicialCompany.objects.filter(pk__in=pervCompany)
        analyst.pervCompany.add(*companies)
        if analyst.pk:
            return redirect('analyst-list')
        else:
            return render(request, 'office/add-analyst.html', context={"companies": company})
    return render(request, 'office/add-analyst.html', context={"companies": company})


def AddRate(request):
    research = ResearchCompany.objects.all()
    company = FinicialCompany.objects.all()
    analyst = FinicialAnalyst.objects.all()
    if request.method == 'POST' and request.FILES['report']:
        CompanyEntered = request.POST.get('CompanyEntered')
        report = request.FILES['report']
        fs = FileSystemStorage()
        filename = fs.save(report.name, report)
        researchCompany = request.POST.get('ResearchCompany')
        AnalayticName = request.POST.get('AnalayticName')
        Recommendation = request.POST.get('Recommendation')
        CurrenncyValue = request.POST.get('CurrenncyValue')
        FairValue = request.POST.get('FairValue')
        MarketValue = request.POST.get('MarketValue')
        rate = Rates(CompanyEntered_id=CompanyEntered, EmpEntered_id=request.user.pk, Recommendation=Recommendation,
                     ResearchCompany_id=researchCompany, AnalayticName_id=AnalayticName, report=report,
                     CurrenncyValue=float(CurrenncyValue), MarketValue=float(MarketValue), FairValue=float(FairValue))
        rate.save()
        if rate.pk:
            return redirect('rates-list')
        else:
            return render(request, 'office/add-rate.html',
                          context={"researches": research, "companies": company, "analysts": analyst})
    return render(request, 'office/add-rate.html',
                  context={"researches": research, "companies": company, "analysts": analyst})


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
    research = ResearchCompany.objects.all()
    rate = Rates.objects.get(pk=pk)
    company = FinicialCompany.objects.all()
    analyst = FinicialAnalyst.objects.all()
    if request.method == 'POST' and request.FILES['report']:
        CompanyEntered = request.POST.get('CompanyEntered')
        report = request.FILES['report']
        fs = FileSystemStorage()
        filename = fs.save(report.name, report)
        researchCompany = request.POST.get('ResearchCompany')
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
        rate.ResearchCompany_id = researchCompany
        rate.EmpEntered_id = request.user.pk
        rate.save()
        if rate.pk:
            return redirect('rate-list')
        else:
            return render(request, 'office/update-rate.html')
    return render(request, 'office/update-rate.html',
                  context={"researches": research, "rate": rate, "companies": company, "analysts": analyst})


def RateDetails(request, pk):
    rate = Rates.objects.get(pk=pk)
    return render(request, 'office/rate-detail.html', context={"rate": rate})


def CompanyDetails(request, pk):
    company = FinicialCompany.objects.get(pk=pk)
    codes = CompanyCode.objects.filter(company=company)
    return render(request, 'office/company-detail.html', context={"company": company, "codes": codes})


def CategoryDetails(request, pk):
    category = CompanyCategory.objects.get(pk=pk)
    companies = FinicialCompany.objects.filter(category=category)
    return render(request, 'office/category-detail.html', context={"category": category, "companies": companies})


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
