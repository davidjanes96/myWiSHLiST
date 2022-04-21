from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid



class Wishlist(models.Model):
    
    class PriorityChoices(models.IntegerChoices):
        low = 1, _('Low')
        medium = 3, _('Medium')
        high = 5, _('High')

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=200)
    priority = models.IntegerField(choices=PriorityChoices.choices, default=PriorityChoices.low)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @property
    def total_products(self):
        try:
            products = self.product_set.all()
            return products.count()
        except AttributeError:
            return 0


    @property
    def grand_total_price(self):
        try:
            products = self.product_set.all()
            total = 0
            for product in products:
                total += product.total_price
            return total
        except AttributeError:
            return 0
    

class Product(models.Model):

    class PriorityChoices(models.IntegerChoices):
        low = 1, _('Low')
        medium = 3, _('Medium')
        high = 5, _('High')

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=2000)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    currency = models.ForeignKey('Currency', on_delete=models.CASCADE)
    url = models.CharField(max_length=2000, blank=True, null=True)
    priority = models.IntegerField(choices=PriorityChoices.choices, default=PriorityChoices.low)
    wishlist = models.ForeignKey('Wishlist', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @property
    def total_price(self):
        return self.price * self.quantity

class Currency(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    tag = models.CharField(max_length=3)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name