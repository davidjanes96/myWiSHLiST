from django.forms import ModelForm
from .models import Wishlist, Product

class WishlistForm(ModelForm):
    class Meta:
        model = Wishlist
        fields = ['title', 'priority']

    def __init__(self, *args, **kwargs):
        super(WishlistForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({
            'class': 'form-control',
            'id': 'title',
            'type': 'text',
            'placeholder': 'Enter wishlist name...',
        })
        self.fields['priority'].widget.attrs.update({
            'class': 'form-select',
            'id': 'priority',
        })



class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'quantity', 'currency', 'url', 'priority']


    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'id': 'item',
            'type': 'text',
            'placeholder': 'Enter item name...'
        })
        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'id': 'price',
            'type': 'number',
            'placeholder': 'Enter item price...'
        })
        self.fields['currency'].empty_label = 'Currency'
        self.fields['currency'].widget.attrs.update({
            'class': 'form-select pt-2',
            'id': 'currency',
        })
        self.fields['quantity'].widget.attrs.update({
            'class': 'form-control',
            'id': 'quantity',
            'type': 'number',
            'placeholder': 'Enter item quantity...'
        })
        self.fields['url'].widget.attrs.update({
            'class': 'form-control',
            'id': 'url',
            'type': 'text',
            'placeholder': 'Enter item url...'
        })
        self.fields['priority'].widget.attrs.update({
            'class': 'form-select',
            'id': 'priority',
        })
 
