from django.urls import path
from . import views

urlpatterns = [
    path('rates/list', views.RatesList, name='rates-list'),
    path('rates/<int:pk>', views.RateDetails, name='rate-details'),
    path('analyst/<int:pk>', views.AnalystDetails, name='analyst-details'),
    path('rates/update/<int:pk>', views.UpdateRate, name='rate-update'),
    path('rates/add', views.AddRate, name='rate-add'),
    path('analyst/update/<int:pk>', views.UpdateAnalyst, name='analyst-update'),
    path('analyst/add', views.AddAnalyst, name='analyst-add'),
    path('analayst/list', views.AnalystsList, name='analyst-list'),
    path('rates/report', views.RatesAllReport.as_view(), name='rates-report'),
    path('analysts/report', views.AnalystsAllReport.as_view(), name='analysts-report'),

]
