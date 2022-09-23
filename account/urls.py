from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),

    path('account/', views.account_view, name="account"),

    path('change_password/', views.CustomPasswordChangeView.as_view(template_name="account/password_change.html"), name="password_change"),
    path('change_password_done/', auth_views.PasswordChangeDoneView.as_view(template_name="account/password_change_done.html"), name="password_change_done"),
]