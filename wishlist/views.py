from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from wishlist.models import Wishlist
from office.models import FinicialCompany
from django.shortcuts import get_object_or_404
from django.contrib import messages

# Create your views here.


@login_required
def add_to_wishlist(request,pk):
   item = get_object_or_404(FinicialCompany,pk=pk)

   wished_Company = Wishlist.objects.get_or_create(wished_company=item,
   user = request.user,
   )
   messages.info(request,'The item was added to your wishlist')
   return redirect('user-home')

@login_required
def view_wishList(request):
    wishes = Wishlist.objects.filter(user= request.user)
    context = {"wishes":wishes}
    return render(request , 'wishlist/allWishes.html' , context)

@login_required
def delete_wishList(request , pk):
    wishes = Wishlist.objects.get(pk=pk)
    wishes.delete()
    return redirect('all_wish')