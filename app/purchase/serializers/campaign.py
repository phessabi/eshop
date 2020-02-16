from rest_framework import serializers

from accounts.models import Vendor
from purchase.models import Campaign


class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = ('id', 'vendor', 'start_datetime', 'end_datetime', 'sale_amount')
        read_only_fields = ('id',)

    def create(self, validated_data):
        vendor_id = validated_data['vendor']
        vendor = Vendor.objects.get(id=vendor_id)
        vendor.clear_campaign()
        return super().create(validated_data)
