from django.urls import path
from . import views

urlpatterns = [
    path('home/<int:pk>', views.user_interface, name='user-interface')
]
