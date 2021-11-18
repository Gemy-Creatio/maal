from django.shortcuts import render
from .models import SeniorOwner , CompaniesArrow , Client
from django.views import View
from django.views.generic.edit import CreateView, UpdateView
from .forms import SeniorOwnerForm , ArrowsForm , ClientForm
from django.urls import reverse
# Create your views here.

class AllUserOwner(View):
    def get(self, request):
        data = CompaniesArrow.objects.order_by('-numberOFArrows')
        return render(request, 'owners/ownerUserlist.html', context={"arrows": data})

class AllSeniorOwners(View):
    def get(self, request):
        data = SeniorOwner.objects.all()
        return render(request, 'owners/AllOwners.html', context={"data": data})


class AllCompaniesArrow(View):
    def get(self, request):
        data = CompaniesArrow.objects.all()
        return render(request, 'owners/AllArrows.html', context={"data": data})

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

def ownerProfile(request , pk):
    data = SeniorOwner.objects.get(pk = pk)
    arrows = CompaniesArrow.objects.filter(owner__id = pk)
    return render(request, 'owners/ownerProfile.html', context={"data": data , "arrows":arrows})  


class AddClient(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'owners/createClient.html'

    def get_success_url(self):
        return reverse('user-home')             