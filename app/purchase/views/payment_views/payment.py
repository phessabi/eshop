from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from purchase.models import Payment, Order
from purchase.serializers import PaymentSerializer


class PaymentView(ListCreateAPIView, GenericViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    def get_queryset(self):
        user = self.request.user
        queryset = Payment.objects.filter(buyer__user=user)
        return queryset

    def create(self, request, *args, **kwargs):
        data = request.data
        data['buyer'] = request.user.buyer.id
        order = Order.objects.get(id=data['order'])
        data['total_price'] = order.total_price
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        payment = serializer.save()
        order = payment.order
        order.status = 2
        order.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
