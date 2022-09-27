from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('account/token/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('account/token/refresh', TokenRefreshView.as_view(), name="token_refresh"),

    path('', views.getRoutes),
    path('wishlists/', views.getWishlists),
    path('wishlists/<str:pk>/', views.getWishlist),
]