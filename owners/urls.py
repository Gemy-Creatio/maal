from django.urls import path
from . import views
from accounts.views import RegisterClient

urlpatterns = [
    path('owners/all', views.AllSeniorOwners.as_view(), name='all-owners'),
    path('owners/add', views.AddOwner.as_view(), name='add-owner'),
    path('owners/update/<int:pk>', views.UpdateOwner.as_view(), name='update-owner'),
    path('arrows/all', views.AllCompaniesArrow.as_view(), name='all-arrows'),
    path('arrows/add', views.AddArrow.as_view(), name='add-arrow'),
    path('arrows/update/<int:pk>', views.UpdateArrow.as_view(), name='update-arrow'),
    path('owners/profile/<int:pk>', views.ownerProfile, name='owner-profile'),
    path('owners/users/all', views.AllUserOwner.as_view(), name='all-user-owners'),
    path('clients/add', RegisterClient.as_view(), name='add-client'),

]