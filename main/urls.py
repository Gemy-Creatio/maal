from django.urls import path
from . import views

urlpatterns = [
    path('', views.master_home, name='user-page'),
    path('dashboard/home', views.home_page, name='home-page'),
    path('reports', views.reports_page, name='reports-page'),

]
