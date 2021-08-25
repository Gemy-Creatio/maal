from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.core.files.storage import FileSystemStorage


def loginPage(request):
    if request.method == 'POST' and request.is_ajax:
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home-page')
        else:
            return JsonResponse({"status": 'Username OR password is incorrect'})
    context = {}
    return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def register_empolyee(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user = User.objects.create_empuser(email=email, first_name=first_name, last_name=last_name,
                                           address=address, password=password, phone=phone)
        if user is not None:
            login(request, user)
            return redirect('home-page')
    context = {}
    return render(request, 'accounts/register.html', context)


def register_admin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user = User.objects.create_superuser(email=email, first_name=first_name, last_name=last_name,
                                             address=address, password=password, phone=phone)
        if user is not None:
            login(request, user)
            return redirect('home-page')
    context = {}
    return render(request, 'accounts/register-admin.html', context)


def user_profile(request):
    user = User.objects.get(pk=request.user.pk)
    return render(request, 'accounts/profile.html', context={"user": user})


def edit_user(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == 'POST':
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user.email = email
        user.phone = phone
        user.address = address
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        if user is not None:
            login(request, user)
            return redirect('home-page')
    context = {}
    return render(request, 'accounts/user-edit.html', context={"user":user})
