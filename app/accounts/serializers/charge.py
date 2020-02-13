from rest_framework import serializers

from accounts.models import Charge


class ChargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Charge
        fields = ('id', 'user', 'amount', 'payment_time')
