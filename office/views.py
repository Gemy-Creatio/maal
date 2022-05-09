from datetime import datetime

from django.core.checks import messages
from django.http import HttpResponse
from maal.utils import render_to_pdf
from django.template.loader import get_template
from django.views import View
from accounts.models import User
from django.shortcuts import render, redirect
from .models import Rates, FinicialCompany, FinicialAnalyst, CompanyCode, CompanyCategory, ResearchCompany, \
    PerviousCompany, EarningsForecast, RateQuarter

from django.core.paginator import Paginator
from django.views.generic import CreateView
from office.forms import *
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from main.models import (
    EarningHeaderSecond
)


class DeleteRate(DeleteView):
    model = Rates
    template_name = 'office/deleteentry.html'
    success_url = reverse_lazy('rates-list')


class DeleteFinicialCompany(DeleteView):
    model = FinicialCompany
    template_name = 'office/deleteentry.html'
    success_url = reverse_lazy('company-list')


class DeleteResearchCompany(DeleteView):
    model = ResearchCompany
    template_name = 'office/deleteentry.html'
    success_url = reverse_lazy('research-list')


class DeleteFinicialAnalyst(DeleteView):
    model = FinicialAnalyst
    template_name = 'office/deleteentry.html'
    success_url = reverse_lazy('analyst-list')


class DeletePervCompany(DeleteView):
    model = PerviousCompany
    template_name = 'office/deleteentry.html'
    success_url = reverse_lazy('pervcompany-list')


class DeleteCompanyCode(DeleteView):
    model = CompanyCode
    template_name = 'office/deleteentry.html'
    success_url = reverse_lazy('company-list')


class DeleteCompanyCategory(DeleteView):
    model = CompanyCode
    template_name = 'office/deleteentry.html'
    success_url = reverse_lazy('category-list')


class DeleteEarningsForecast(DeleteView):
    model = EarningsForecast
    template_name = 'office/deleteentry.html'
    success_url = reverse_lazy('expectations-list')


def RatesList(request):
    rates = Rates.objects.all().order_by('-pk')
    paginator = Paginator(rates, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'office/rates-list.html', context={"rates": page_obj})


def Research_List(request):
    companies = ResearchCompany.objects.all().order_by('-pk')
    paginator = Paginator(companies, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'office/research_list.html', context={"companies": page_obj})


def Company_List(request):
    companies = FinicialCompany.objects.all().order_by('-pk')
    paginator = Paginator(companies, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'office/company_list.html', context={"companies": page_obj})


def Category_List(request):
    category = CompanyCategory.objects.all().order_by('-pk')
    paginator = Paginator(category, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'office/catgory-list.html', context={"categories": page_obj})


class AddCategory(CreateView):
    form_class = CategoryForm
    model = CompanyCategory
    template_name = 'office/add-category.html'

    def form_valid(self, form):
        category = form.save(commit=True)
        category.EmpEntered = self.request.user
        category.save()
        return super(AddCategory, self).form_valid(form)

    def get_success_url(self):
        return reverse('category-list')


class UpdateCategory(UpdateView):
    form_class = CategoryForm
    model = CompanyCategory
    template_name = 'office/edit-category.html'

    def form_valid(self, form):
        category = form.save(commit=True)
        category.EmpEntered = self.request.user
        category.save()
        return super(UpdateCategory, self).form_valid(form)

    def get_success_url(self):
        return reverse('category-list')


class AddCode(CreateView):
    form_class = CompanyCodeForm
    model = CompanyCode
    template_name = 'office/add-code.html'

    def get_success_url(self):
        return reverse('company-list')


class UpdateCode(UpdateView):
    form_class = CompanyCodeForm
    model = CompanyCode
    template_name = 'office/update-code.html'

    def get_success_url(self):
        return reverse('company-list')


class AddReserchCompany(CreateView):
    form_class = ResearchCompanyForm
    model = ResearchCompany
    template_name = 'office/add-research.html'

    def form_valid(self, form):
        research = form.save(commit=True)
        research.EmpEntered = self.request.user
        research.save()
        return super(AddReserchCompany, self).form_valid(form)

    def get_success_url(self):
        return reverse('research-list')


class UpdateReserchCompany(UpdateView):
    form_class = ResearchCompanyForm
    model = ResearchCompany
    template_name = 'office/edit-research.html'

    def form_valid(self, form):
        research = form.save(commit=True)
        research.EmpEntered = self.request.user
        research.save()
        return super(UpdateReserchCompany, self).form_valid(form)

    def get_success_url(self):
        return reverse('research-list')


class AddCompany(CreateView):
    form_class = FinicalCompanyForm
    model = models.FinicialCompany
    template_name = 'office/add-company.html'

    def form_valid(self, form):
        company = form.save(commit=True)
        company.EmpEntered = self.request.user
        company.save()
        return super(AddCompany, self).form_valid(form)

    def get_success_url(self):
        return reverse('company-list')


class EditCompany(UpdateView):
    form_class = FinicalCompanyForm
    model = models.FinicialCompany
    template_name = 'office/edit-company.html'

    def form_valid(self, form):
        company = form.save(commit=True)
        company.EmpEntered = self.request.user
        company.logo = form.cleaned_data['logo']
        company.save()
        return super(EditCompany, self).form_valid(form)

    def get_success_url(self):
        return reverse('company-list')


def AnalystsList(request):
    analayts = FinicialAnalyst.objects.all().order_by('-pk')
    paginator = Paginator(analayts, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'office/analysts-list.html', context={"analayts": page_obj})


class AddAnalyst(CreateView):
    model = models.FinicialAnalyst
    template_name = 'office/add-analyst.html'
    form_class = AnalystForm

    def get_success_url(self):
        return reverse('analyst-list')


class AddRate(CreateView):
    model = models.Rates
    template_name = 'office/add-rate.html'
    form_class = RateForm

    def get_success_url(self):
        return reverse('rates-list')


class AddExpect(CreateView):
    form_class = ExpectationForm
    model = models.EarningsForecast
    template_name = 'office/add-expectation.html'

    def get_success_url(self):
        return reverse('expectations-list')


class UpdateExpect(UpdateView):
    form_class = ExpectationForm
    model = models.EarningsForecast
    template_name = 'office/edit-expect.html'

    def get_success_url(self):
        return reverse('expectations-list')


class UpdateRate(UpdateView):
    form_class = RateForm
    template_name = 'office/update-rate.html'
    model = models.Rates

    def get_success_url(self):
        return reverse('rates-list')


class UpdateAnalyst(UpdateView):
    form_class = AnalystForm
    template_name = 'office/update-analyst.html'
    model = models.FinicialAnalyst

    def get_success_url(self):
        return reverse('analyst-list')


def RateDetails(request, pk):
    rate = Rates.objects.get(pk=pk)
    return render(request, 'office/rate-detail.html', context={"rate": rate})


def CompanyDetails(request, pk):
    company = FinicialCompany.objects.get(pk=pk)
    codes = CompanyCode.objects.filter(company=company).order_by('-pk')
    return render(request, 'office/company-detail.html', context={"company": company, "codes": codes})


def CategoryDetails(request, pk):
    category = CompanyCategory.objects.get(pk=pk)
    companies = FinicialCompany.objects.filter(category=category).order_by('-pk')
    return render(request, 'office/category-detail.html', context={"category": category, "companies": companies})


def AnalystDetails(request, pk):
    analyst = FinicialAnalyst.objects.get(pk=pk)
    return render(request, 'office/analyst-detail.html', context={"analyst": analyst})


class RatesAllReport(View):
    def get(self, request, *args, **kwargs):
        template = get_template('rates-all-pdf.html')
        rates = Rates.objects.all().order_by('-pk')
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
        analayts = FinicialAnalyst.objects.all().order_by('-pk')
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


def PervCompanyList(request, pk):
    pervcopmainies = PerviousCompany.objects.filter(analyst_id=pk).order_by('-pk')
    analyst = FinicialAnalyst.objects.get(pk=pk)
    return render(request, 'office/percompany-list.html', context={"companies": pervcopmainies, 'analyst': analyst})


def addPervCompany(request, pk):
    if request.method == 'POST':
        company = request.POST.get('company')
        job = request.POST.get('job')
        perv = PerviousCompany(job=job, company=company, analyst_id=pk)
        perv.save()
        if perv.pk:
            return redirect('pervcompany-list', pk=pk)
        else:
            return render(request, 'office/add-pervcompany.html')
    return render(request, 'office/add-pervcompany.html')


def ExpectationList(request):
    expects = EarningsForecast.objects.order_by('-pk')
    paginator = Paginator(expects, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    headers = EarningHeaderSecond.get_solo()
    context = {
        "expectations": page_obj,
        "headers": headers
    }
    return render(request, 'office/expectation-list.html', context=context)

