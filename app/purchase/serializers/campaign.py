from rest_framework import serializers

from purchase.models import Campaign


class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = ('id', 'vendor', 'start_datetime', 'end_datetime', 'sale_amount')
        read_only_fields = ('id',)

    def to_internal_value(self, data):
        user = self.context['request'].user
        vendor_id = user.vendor.id
        data['vendor'] = vendor_id
        return super().to_internal_value(data)
