from rest_framework import serializers

from accounts.models import Vendor


class VendorProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vendor
        fields = ('id', 'name', 'credit', 'commission')
        read_only_fields = ('id', 'commission')
