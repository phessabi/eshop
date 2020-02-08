from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from purchase.models import Order
from purchase.serializers import OrderSerializer


class OrderViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def get_queryset(self):
        user = self.request.user
        queryset = Order.objects.filter(buyer__user=user, status=2)
        return queryset
