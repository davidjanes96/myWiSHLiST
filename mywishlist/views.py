from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse

from wishlists.models import Wishlist, Product, Currency


def home_view(request):
    wishlists = Wishlist.objects.all()
    context = {'wishlists': wishlists, }
    return render(request, 'index.html', context)