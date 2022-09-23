from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from .forms import CustomPasswordResetForm, CustomSetPasswordForm


def home_view(request):
    if request.user.is_authenticated:
        account = request.user.account
        wishlists = account.wishlist_set.all()
        context = {
            'wishlists': wishlists,
            'account': account,
            }
    else:
        context = {}
    return render(request, 'index.html', context)


class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = CustomSetPasswordForm