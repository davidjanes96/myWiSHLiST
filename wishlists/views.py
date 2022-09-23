
from locale import currency
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .utils import paginateWishlists
from .models import Wishlist
from .forms import WishlistForm, ProductForm


@login_required(login_url="login")
def get_all_wishlists(request):
    account = request.user.account
    wishlists = account.wishlist_set.all()
    text_message = ''
    search_query = ''

    if not wishlists:
        text_message = "You don't have any wishlists."

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        wishlists = account.wishlist_set.filter(title__icontains=search_query)
        if not wishlists:
            text_message = "No wishlists found."        

    custom_range, wishlists = paginateWishlists(request, wishlists, 10)

    context = {
        'wishlists': wishlists,
        'search_query': search_query,
        'text_message': text_message,
        'custom_range': custom_range,
        }    
    return render(request, 'wishlists/wishlists.html', context)
    

@login_required(login_url="login")
def get_wishlist_details(request, pk):
    account = request.user.account
    wishlists = account.wishlist_set.all()
    error_message = ''
    text_message = ''
    search_query = ''

    if not wishlists:
        text_message = "You don't have any wishlists."

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        wishlists = account.wishlist_set.filter(title__icontains=search_query)
        if not wishlists:
            text_message = "No wishlists found."

    wishlist = Wishlist.objects.get(id=pk)
    products = wishlist.product_set.all().order_by('name')

    #sort conditions
    if request.GET.get('sort') == 'name-asc':
        products = wishlist.product_set.all().order_by('name')
    elif request.GET.get('sort') == 'name-desc':
        products = wishlist.product_set.all().order_by('-name')
    elif request.GET.get('sort') == 'price-asc':
        products = wishlist.product_set.all().order_by('price')
    elif request.GET.get('sort') == 'price-desc':
        products = wishlist.product_set.all().order_by('-price')
    elif request.GET.get('sort') == 'quantity-asc':
        products = wishlist.product_set.all().order_by('quantity')
    elif request.GET.get('sort') == 'quantity-desc':
        products = wishlist.product_set.all().order_by('-quantity')
    elif request.GET.get('sort') == 'priority-asc':
        products = wishlist.product_set.all().order_by('priority')
    elif request.GET.get('sort') == 'priority-desc':
        products = wishlist.product_set.all().order_by('-priority')

    #currency error handling
    currency_1 = wishlist.product_set.all().values_list('currency__tag', flat=True).order_by('currency__name').first()
    currency_2 = wishlist.product_set.all().values_list('currency__tag', flat=True).order_by('-currency__name').first()

    if currency_1 != currency_2:
        error_message = "Please match item currencies to display total value."

    custom_range, wishlists = paginateWishlists(request, wishlists, 10)

    context = {
        'wishlist': wishlist, 
        'wishlists': wishlists,
        'search_query': search_query,
        'text_message': text_message,
        'error_message': error_message,
        'currency_1': currency_1,
        'custom_range': custom_range,
        'products': products,
        }
    return render (request, 'wishlists/wishlist.html', context)


@login_required(login_url="login")
def create_wishlist(request):
    page = 'create-wishlist'
    account = request.user.account

    form = WishlistForm()

    if request.method == 'POST':
        form = WishlistForm(request.POST)
        if form.is_valid():
            wishlist = form.save(commit=False)
            wishlist.owner = account
            form.save()
            messages.success(request, 'Wishlist created successfully.')
            return redirect('wishlist', pk=wishlist.id)

    context = {'form': form, 'page': page}
    return render(request, 'wishlists/wishlist_form.html', context)


@login_required(login_url="login")
def update_wishlist(request, pk):
    page = 'update-wishlist'
    account = request.user.account
    wishlist = account.wishlist_set.get(id=pk)
    form = WishlistForm(instance = wishlist)

    if request.method == 'POST':
        form = WishlistForm(request.POST, instance=wishlist)
        if form.is_valid():
            form.save()
            messages.success(request, 'Wishlist updated successfully.')
            return redirect('wishlist', pk=wishlist.id)

    context = {'form': form, 'page': page}
    return render(request, 'wishlists/wishlist_form.html', context)


@login_required(login_url="login") 
def delete_wishlist(request, pk):
    account = request.user.account
    wishlist = account.wishlist_set.get(id=pk)
    if request.method == 'POST':
        wishlist.delete()
        messages.success(request, 'Wishlist deleted successfully.')
        return redirect('wishlists')

    context = {'object': wishlist}
    return render(request, 'wishlists/delete_template.html', context)


@login_required(login_url="login") 
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


@login_required(login_url="login") 
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


@login_required(login_url="login") 
def delete_product(request, pk, productPK):
    wishlist = Wishlist.objects.get(id=pk)
    product = wishlist.product_set.get(id=productPK)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Item deleted successfully.')
        return redirect('wishlist', pk=wishlist.id)

    context = {'object': product}
    return render(request, 'wishlists/delete_template.html', context)