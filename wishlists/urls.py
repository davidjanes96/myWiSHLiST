from django.urls import path
from . import views

urlpatterns = [
    path('wishlists/', views.get_all_wishlists, name="wishlists"),
    path('wishlist/<str:pk>/', views.get_wishlist_details, name="wishlist"),

    path('create-wishlist/', views.create_wishlist, name="create-wishlist"),
    path('update-wishlist/<str:pk>', views.update_wishlist, name="update-wishlist"),
    path('delete-wishlist/<str:pk>', views.delete_wishlist, name="delete-wishlist"),

    path('wishlist/<str:pk>/create-product/', views.create_product, name="create-product"),
    path('wishlist/<str:pk>/update-product/<str:productPK>', views.update_product, name="update-product"),
    path('wishlist/<str:pk>/delete-product/<str:productPK>', views.delete_product, name="delete-product"),

]