from django.shortcuts import render
from .models import SeniorOwner, CompaniesArrow
from django.views import View
from django.views.generic.edit import CreateView, UpdateView
from .forms import SeniorOwnerForm, ArrowsForm
from django.urls import reverse
from django.core.paginator import Paginator


# Create your views here.

class AllUserOwner(View):
    def get(self, request):
        data = CompaniesArrow.objects.order_by('-numberOFArrows')
        arrows = SeniorOwner.objects.all()
        return render(request, 'owners/ownerUserlist.html', context={"data": arrows, "companyarrows": data})


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
