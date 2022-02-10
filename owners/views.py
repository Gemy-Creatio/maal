from django.shortcuts import render
from django.views.generic import ListView

from .models import SeniorOwner, CompaniesArrow, FinicalCompaniesArrow
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import SeniorOwnerForm, ArrowsForm, CompaniesArrowsForm
from django.urls import reverse, reverse_lazy
from django.core.paginator import Paginator


# Create your views here.

class AllUserOwner(View):
    def get(self, request):
        data = FinicalCompaniesArrow.objects.order_by('-numberOFArrows')
        arrows = SeniorOwner.objects.all()
        seniorArrows = CompaniesArrow.objects.all()
        return render(request, 'owners/ownerUserlist.html',
                      context={"data": arrows, "companyarrows": data, "seniorArrows": seniorArrows})


class AllSeniorOwners(View):
    def get(self, request):
        data = SeniorOwner.objects.all()
        paginator = Paginator(data, 8)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'owners/AllOwners.html', context={"data": page_obj})


class AllCompaniesArrow(View):
    def get(self, request):
        data = CompaniesArrow.objects.all()
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
    data = SeniorOwner.objects.filter(pk=pk)
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
