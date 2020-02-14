from rest_framework import serializers
from products.models import Product
from products.serializers.specification import SpecificationSerializer


class ProductSerializer(serializers.ModelSerializer):
    specifications = SpecificationSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'category', 'price', 'express', 'specifications', 'vendor')
        read_only_fields = ('id', 'deleted', 'specifications')

    def create(self, validated_data):
        validated_data['vendor_id'] = self.context.get('vendor_id')
        return super().create(validated_data)
