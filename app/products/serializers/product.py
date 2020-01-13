from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'category', 'price', 'express', 'deleted')
        read_only_fields = ('id',)

    def create(self, validated_data):
        validated_data['vendor'] = self.context.get('vendor')
        return super().create(validated_data)
