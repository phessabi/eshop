from rest_framework import serializers

from accounts.models import Buyer


class PhoneAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = ('address', 'phone_number')
