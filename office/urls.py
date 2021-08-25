from django.urls import path
from . import views

urlpatterns = [
    path('rates/list', views.RatesList, name='rates-list'),
    path('company/list', views.Company_List, name='company-list'),
    path('rates/<int:pk>', views.RateDetails, name='rate-details'),
    path('category/<int:pk>', views.CategoryDetails, name='category-details'),
    path('analyst/<int:pk>', views.AnalystDetails, name='analyst-details'),
    path('company/<int:pk>', views.CompanyDetails, name='company-details'),
    path('rates/update/<int:pk>', views.UpdateRate, name='rate-update'),
    path('rates/add', views.AddRate, name='rate-add'),
    path('category/update/<int:pk>', views.EditCategory, name='category-update'),
    path('company/update/<int:pk>', views.EditCompany, name='company-update'),
    path('analyst/update/<int:pk>', views.UpdateAnalyst, name='analyst-update'),
    path('analyst/add', views.AddAnalyst, name='analyst-add'),
    path('company/add', views.AddCompany, name='company-add'),
    path('category/add', views.AddCategory, name='category-add'),
    path('category/list', views.Category_List, name='category-list'),
    path('analayst/list', views.AnalystsList, name='analyst-list'),
    path('rates/report', views.RatesAllReport.as_view(), name='rates-report'),
    path('analysts/report', views.AnalystsAllReport.as_view(), name='analysts-report'),

]
