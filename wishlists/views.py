
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages

from .models import Wishlist
from .forms import WishlistForm, ProductForm

def get_all_wishlists(request):
    wishlists = Wishlist.objects.all()
    context = {'wishlists': wishlists, }
    return render(request, 'wishlists/wishlists.html', context)


def get_wishlist_details(request, pk):
    wishlists = Wishlist.objects.all()
    wishlist = Wishlist.objects.get(id=pk)
    context = {
        'wishlist': wishlist, 
        'wishlists': wishlists,
        }
    return render (request, 'wishlists/wishlist.html', context)



def create_wishlist(request):
    form = WishlistForm()

    if request.method == 'POST':
        form = WishlistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('wishlists')

    context = {'form': form}
    return render(request, 'wishlists/wishlist_form.html', context)



def update_wishlist(request, pk):
    wishlist = Wishlist.objects.get(id=pk)
    form = WishlistForm(instance = wishlist)

    if request.method == 'POST':
        form = WishlistForm(request.POST, instance=wishlist)
        if form.is_valid():
            form.save()
            return redirect('wishlists')

    context = {'form': form}
    return render(request, 'wishlists/wishlist_form.html', context)


def delete_wishlist(request, pk):
    wishlist = Wishlist.objects.get(id=pk)
    if request.method == 'POST':
        wishlist.delete()
        return redirect('wishlists')

    context = {'object': wishlist}
    return render(request, 'wishlists/delete_template.html', context)


def create_product(request, pk):
    wishlist = Wishlist.objects.get(id=pk)
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        product = form.save(commit=False)
        product.wishlist = wishlist
        if form.is_valid():
            product.save()
            messages.success(request, 'Item added successfully.')
            return redirect ('wishlist', pk=wishlist.id)

    context = {
        'form': form,
        'wishlist': wishlist,
        }
    return render(request, 'wishlists/product_form.html', context)



def update_product(request, pk, productPK):
    wishlist = Wishlist.objects.get(id=pk)
    product = wishlist.product_set.get(id=productPK)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        product = form.save(commit=False)
        product.wishlist = wishlist
        if form.is_valid():
            product.save()
            messages.success(request, 'Item updated successfully.')
            return redirect ('wishlist', pk=wishlist.id)

    context = {
        'form': form,
        'wishlist': wishlist,
        'product': product,
        }
    return render(request, 'wishlists/product_form.html', context)


def delete_product(request, pk, productPK):
    wishlist = Wishlist.objects.get(id=pk)
    product = wishlist.product_set.get(id=productPK)
    if request.method == 'POST':
        product.delete()
        return redirect('wishlist', pk=wishlist.id)

    context = {'object': wishlist}
    return render(request, 'wishlists/delete_template.html', context)