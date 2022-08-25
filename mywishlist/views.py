from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse

from wishlists.models import Wishlist, Product, Currency


def home_view(request):
    if request.user.is_authenticated:
        account = request.user.account
        wishlists = account.wishlist_set.all()
        context = {
            'wishlists': wishlists,
            'account': account
            }
    else:
        context = {}
    return render(request, 'index.html', context)