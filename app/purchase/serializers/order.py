from rest_framework import serializers

from products.serializers import ProductSerializer
from purchase.models import Order


class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'buyer', 'products', 'address', 'phone_number', 'delivery_date', 'total_price')
