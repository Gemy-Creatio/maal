from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_page, name='user-page'),
    path('rates/home', views.home_page, name='home-page'),
    path('reports', views.reports_page, name='reports-page'),

]
