from django.contrib import admin
from .models import Currency, Product, Wishlist

# Register your models here.

admin.site.register(Currency)
admin.site.register(Product)
admin.site.register(Wishlist)
