from django.urls import path
from . import views

urlpatterns = [
    path('rates/list', views.RatesList, name='rates-list'),
    path('rates/<int:pk>', views.RateDetails, name='rate-details'),
    path('rates/update/<int:pk>', views.UpdateRate, name='rate-update'),
    path('rates/add', views.AddRate, name='rate-add'),
    path('rates/report', views.RatesAllReport.as_view(), name='rates-report'),

]
