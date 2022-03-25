from django.shortcuts import redirect, render
from django.views.generic import ListView
import codecs
import csv

from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from .models import SeniorOwner, CompaniesArrow, FinicalCompaniesArrow ,CSVUpdate
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import SeniorOwnerForm, ArrowsForm, CompaniesArrowsForm
from django.urls import reverse, reverse_lazy
from django.core.paginator import Paginator
from office.models  import (
    FinicialCompany
)

fs = FileSystemStorage(location='csv/')


# Create your views here.

class AllUserOwner(View):
    def get(self, request):
        companyarrows = CompaniesArrow.objects.exclude(owner_type=1).order_by('-pk')[:8]
        arrows_page = SeniorOwner.objects.all().order_by('-pk')[:8]
        seniorArrows_page = CompaniesArrow.objects.filter(owner_type=1).order_by('-pk')
        paginator = Paginator(seniorArrows_page, 8)
        page_number = request.GET.get('page')
        seniorArrows = paginator.get_page(page_number)
        return render(request, 'owners/ownerUserlist.html',
                      context={"data": arrows_page, "companyarrows": companyarrows, "seniorArrows": seniorArrows})

class AllSeniorArrowsUser(View):
    def get(self, request):
        arrows_page = SeniorOwner.objects.all().order_by('-pk')[:8]
        paginator = Paginator(arrows_page, 8)
        page_number = request.GET.get('page')
        seniorArrows = paginator.get_page(page_number)
        return render(request, 'owners/ownerseniorlist.html',context={"data":seniorArrows})






class AllCompanyArrowsUser(View):
    def get(self , request):
        arrows = CompaniesArrow.objects.exclude(owner_type=1).order_by('-pk')
        paginator = Paginator(arrows, 8)
        page_number = request.GET.get('page')
        Arrows = paginator.get_page(page_number)
        return render(request , 'owners/ownercompaniesall.html' ,context={"companyarrows":Arrows})

class AllSeniorOwners(View):
    def get(self, request):
        data = SeniorOwner.objects.all().order_by('-pk')
        paginator = Paginator(data, 8)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'owners/AllOwners.html', context={"data": page_obj})


class AllCompaniesArrow(View):
    def get(self, request):
        data = CompaniesArrow.objects.all().order_by('-pk')
        paginator = Paginator(data, 8)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'owners/AllArrows.html', context={"data": page_obj})


class AddOwner(CreateView):
    model = SeniorOwner
    form_class = SeniorOwnerForm
    template_name = 'owners/createOwner.html'

    def get_success_url(self):
        return reverse('all-owners')


class UpdateOwner(UpdateView):
    model = SeniorOwner
    form_class = SeniorOwnerForm
    template_name = 'owners/updateowner.html'

    def get_success_url(self):
        return reverse('all-owners')


class AddArrow(CreateView):
    model = CompaniesArrow
    form_class = ArrowsForm
    template_name = 'owners/createarrows.html'

    def get_success_url(self):
        return reverse('all-arrows')


class UpdateArrow(UpdateView):
    model = CompaniesArrow
    form_class = ArrowsForm
    template_name = 'owners/updatearrows.html'

    def get_success_url(self):
        return reverse('all-arrows')


def ownerProfile(request, pk):
    data = SeniorOwner.objects.filter(pk=pk).order_by('-pk')
    return render(request, 'owners/ownerProfile.html', context={"data": data})


class AllCompanyArrowsOwners(ListView):
    # specify the model for list view
    model = FinicalCompaniesArrow
    template_name = 'owners/CompanyArrowsList.html'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AddCompanyArrows(CreateView):
    model = FinicalCompaniesArrow
    form_class = CompaniesArrowsForm
    template_name = 'owners/AddCompanyArrows.html'

    def get_success_url(self):
        return reverse('all-AllCompanyOwners')


class DeleteOwner(DeleteView):
    model = SeniorOwner
    template_name = 'office/deleteentry.html'
    success_url = reverse_lazy('all-owners')


class DeleteCompanyOwner(DeleteView):
    model = FinicalCompaniesArrow
    template_name = 'office/deleteentry.html'
    success_url = reverse_lazy('all-AllCompanyOwners')


class DeleteOwnerCompany(DeleteView):
    model = CompaniesArrow
    template_name = 'office/deleteentry.html'
    success_url = reverse_lazy('all-arrows')


class EditCompanyArrows(UpdateView):
    model = FinicalCompaniesArrow
    form_class = CompaniesArrowsForm
    template_name = 'owners/EditCompanyArrows.html'

    def get_success_url(self):
        return reverse('all-AllCompanyOwners')




class UpdateCompaniesByCSV(View):
    def get(self , request):
        return render(request , 'owners/addbycsv.html')
    def post(self , request):
        file = request.FILES["file"]
        content = file.read()  # these are bytes
        file_content = ContentFile(content)
        file_name = fs.save(
            "_tmp.csv", file_content
        )
        csv_obj = CSVUpdate(file_csv = file)
        csv_obj.save()
        tmp_file = fs.path(file_name)

        csv_file = open(tmp_file, errors="ignore")
        reader = csv.reader(csv_file)
        next(reader)
        
        company_list = []
        for id_, row in enumerate(reader):
            (
                pk,
                arrow_value
            ) = row
            company_list.append(
                FinicialCompany(
                    pk=pk,
                    arrow_value=arrow_value,
                )
            )

        FinicialCompany.objects.bulk_update(company_list , ['arrow_value'])
        return redirect('company-list')
