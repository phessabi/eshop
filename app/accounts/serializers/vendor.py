from rest_framework import serializers

from accounts.models import Vendor
from purchase.serializers import CampaignSerializer


class VendorSerializer(serializers.ModelSerializer):
    campaign = CampaignSerializer(allow_null=True)

    class Meta:
        model = Vendor
        fields = ('id', 'name', 'campaign')
