from rest_framework import serializers
from products.models import Product
from products.serializers.specification import SpecificationSerializer


class ProductSerializer(serializers.ModelSerializer):
    specifications = SpecificationSerializer(many=True, read_only=True)
    category_name = serializers.SerializerMethodField()
    vendor_name = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'title', 'category', 'category_name', 'price', 'express', 'specifications', 'vendor', 'vendor_name')
        read_only_fields = ('id', 'specifications')

    @staticmethod
    def get_category_name(instance: Product):
        return instance.category.name

    @staticmethod
    def get_vendor_name(instance: Product):
        return instance.vendor.name

    def create(self, validated_data):
        validated_data['vendor_id'] = self.context.get('vendor_id')
        return super().create(validated_data)


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = 'image'
