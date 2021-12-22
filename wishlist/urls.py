from django.urls import path
from . import views

urlpatterns = [
path("add-wish/<int:pk>/", views.add_to_wishlist, name="add_wish"),
path("add-wish/async/", views.add_to_wishlist_aysnc, name="add_wish_aync"),
path("all-wishes", views.view_wishList, name="all_wish"),
path("delete-wish/<int:pk>/", views.delete_wishList, name="delete_wish"),
path("companies/ajax", views.all_cats_ajax, name="comp_aiax"),

]