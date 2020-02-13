from rest_framework import serializers

from accounts.models import Buyer


class BuyerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = ('id', 'name', 'address', 'phone_number', 'credit')
        read_only_fields = ('id',)
