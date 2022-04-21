from django.forms import ModelForm
from .models import Wishlist, Product

class WishlistForm(ModelForm):
    class Meta:
        model = Wishlist
        fields = ['title', 'priority']


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'quantity', 'currency', 'url', 'priority']