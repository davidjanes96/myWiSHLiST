from pyexpat import model
from rest_framework import serializers
from wishlists.models import Wishlist, Product
from account.models import Account

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class WishlistSerializer(serializers.ModelSerializer):
    owner = AccountSerializer(many=False)
    products = serializers.SerializerMethodField()

    class Meta:
        model = Wishlist
        fields = '__all__'

    def get_products(self, obj):
        products = obj.product_set.all()
        serializer = ProductSerializer(products, many=True)
        return serializer.data