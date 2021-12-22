from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from wishlist.models import Wishlist
from django.shortcuts import get_object_or_404
from django.contrib import messages
from office.models import CompanyCategory, FinicialCompany
from django.core import serializers
from django.http import JsonResponse


# Create your views here.

def all_cats_ajax(request):
    if request.method == "POST" and request.is_ajax():
        companies = FinicialCompany.objects.filter(category_id=request.POST.get('cat', '')).values()
        data = list(companies)
        return JsonResponse(data, safe=False)


@login_required
def add_to_wishlist(request, pk):
    item = get_object_or_404(FinicialCompany, pk=pk)

    wished_Company = Wishlist.objects.get_or_create(wished_company=item,
                                                    user=request.user,
                                                    )
    request.session['wish_count'] = Wishlist.objects.filter(user=request.user).count()
    messages.info(request, 'The item was added to your wishlist')
    return redirect('user-home')


@login_required
def view_wishList(request):
    wishes = Wishlist.objects.filter(user=request.user)
    cats = CompanyCategory.objects.all()
    context = {"wishes": wishes, 'cats': cats}
    return render(request, 'wishlist/allWishes.html', context)


def add_to_wishlist_aysnc(request):
    if request.method == 'POST' and request.is_ajax():
        id = request.POST.get('comp_id')
        company = FinicialCompany.objects.get(pk=id)
        wished_Company = Wishlist.objects.get_or_create(wished_company=company,
                                                        user=request.user,
                                                        )
        request.session['wish_count'] = Wishlist.objects.filter(user=request.user).count()
        return redirect('user-home')


@login_required
def delete_wishList(request, pk):
    wishes = Wishlist.objects.get(pk=pk)
    wishes.delete()
    request.session['wish_count'] = Wishlist.objects.filter(user=request.user).count()
    return redirect('all_wish')
