from rest_framework import serializers
from products.models import Product
from products.serializers.specification import SpecificationSerializer
from purchase.serializers import CampaignSerializer


class ProductSerializer(serializers.ModelSerializer):
    specifications = SpecificationSerializer(many=True, read_only=True)
    campaign = CampaignSerializer(source='vendor.campaign', read_only=True, allow_null=True)

    class Meta:
        model = Product
        fields = (
            'id', 'title', 'category', 'price', 'price_after_sale', 'express', 'specifications', 'vendor', 'campaign',
        )
        read_only_fields = ('id', 'specifications', 'price_after_sale', 'campaign')

    def create(self, validated_data):
        validated_data['vendor_id'] = self.context.get('vendor_id')
        return super().create(validated_data)
