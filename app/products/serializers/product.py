from rest_framework import serializers
from products.models import Product
from products.serializers.specification import SpecificationSerializer


class ProductSerializer(serializers.ModelSerializer):
    specifications = SpecificationSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'category', 'price', 'express', 'archived', 'specifications')
        read_only_fields = ('id', 'deleted')

    def create(self, validated_data):
        validated_data['vendor_id'] = self.context.get('vendor_id')
        return super().create(validated_data)
