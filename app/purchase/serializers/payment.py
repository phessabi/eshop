from rest_framework import serializers

from purchase.models import Payment, Order


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('id', 'buyer', 'order', 'total_price', 'payment_time')

    def to_internal_value(self, data):
        user = self.context['request'].user
        buyer_id = user.buyer.id
        data['buyer'] = buyer_id

        order = Order.objects.get(id=data['order'])
        data['total_price'] = order.total_price
        return super().to_internal_value(data)

    def validate(self, attrs):
        validated_data = super().validate(attrs)
        buyer = validated_data['buyer']
        total_price = validated_data['total_price']
        if buyer.credit < total_price:
            raise serializers.ValidationError('اعتبار کافی برای پرداخت موجود نیست.')
        return validated_data
