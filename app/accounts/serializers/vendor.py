from rest_framework import serializers

from accounts.models import Vendor


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ('user', 'name', 'credit')
