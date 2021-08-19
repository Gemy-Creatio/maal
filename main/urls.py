from django.urls import path
from . import views
from accounts.views import loginPage

urlpatterns = [
    path('', loginPage, name='login-page'),
    path('rates/home', views.home_page, name='home-page'),
    path('reports', views.reports_page, name='reports-page'),

]
