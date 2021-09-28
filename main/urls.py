from django.urls import path
from . import views
from userInterface.views import user_home

urlpatterns = [
    path('', user_home, name='user-page'),
    path('dashboard/home', views.home_page, name='home-page'),
    path('reports', views.reports_page, name='reports-page'),
    path('analysts/ajax', views.analysts_ajax, name='analyst-ajax'),

]
