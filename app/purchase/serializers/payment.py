from rest_framework import serializers

from purchase.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('id', 'buyer', 'order', 'total_price', 'payment_time')
