from django.urls import path
from . import views
from accounts.views import RegisterClient

urlpatterns = [
    path('owners/all', views.AllSeniorOwners.as_view(), name='all-owners'),
    path('owners/add', views.AddOwner.as_view(), name='add-owner'),
    path('owners/update/<int:pk>', views.UpdateOwner.as_view(), name='update-owner'),
    path('owners/delete/<int:pk>', views.DeleteOwner.as_view(), name='delete-owner'),
    path('company/owners/all', views.AllCompanyArrowsOwners.as_view(), name='all-AllCompanyOwners'),
    path('company/owners/add', views.AddCompanyArrows.as_view(), name='add-ِAddCompanyArrows'),
    path('company/owners/delete/<int:pk>', views.DeleteCompanyOwner.as_view(), name='delete-company-Arrows'),
    path('company/owners/update/<int:pk>', views.EditCompanyArrows.as_view(), name='update-company-Arrows'),
    path('arrows/all', views.AllCompaniesArrow.as_view(), name='all-arrows'),
    path('arrows/add', views.AddArrow.as_view(), name='add-arrow'),
    path('arrows/delete/<int:pk>', views.DeleteOwnerCompany.as_view(), name='delete-arrow'),
    path('arrows/update/<int:pk>', views.UpdateArrow.as_view(), name='update-arrow'),
    path('owners/profile/<int:pk>', views.ownerProfile, name='owner-profile'),
    path('owners/users/all', views.AllUserOwner.as_view(), name='all-user-owners'),
    path('clients/add', RegisterClient.as_view(), name='add-client'),
    path('all/companiesarrows', views.AllCompanyArrowsUser.as_view(), name='arrows-comp-users'),
    path('all/seniors', views.AllSeniorArrowsUser.as_view(), name='arrows-sen-users'),
    path('update/csv', views.UpdateCompaniesByCSV.as_view(), name='update-csv'),

]