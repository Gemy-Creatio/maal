from django.urls import path
from . import views

urlpatterns = [
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('profile', views.user_profile, name='profile'),
    path('user-edit/<int:pk>', views.edit_user, name='user-edit'),
    path('register-employee', views.register_empolyee, name='register-employee'),
    path('register-admin', views.register_admin, name='register-admin'),

]
