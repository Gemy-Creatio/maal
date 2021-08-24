from django.shortcuts import render


def home_page(request):
    return render(request, 'main/home.html')


def reports_page(request):
    return render(request, 'main/reports.html')


def user_page(request):
    return render(request, 'main/user-home.html')
