from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'category', 'price', 'express', 'archived')
        read_only_fields = ('id', 'deleted')

    def create(self, validated_data):
        validated_data['vendor_id'] = self.context.get('vendor_id')
        return super().create(validated_data)
