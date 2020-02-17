from rest_framework import serializers

from products.serializers import ProductSerializer
from purchase.models import Cart


class CartSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ('id', 'products', 'total_price_before_sale', 'total_price')
