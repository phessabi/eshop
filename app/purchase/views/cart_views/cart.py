from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from purchase.models import Cart
from purchase.serializers.cart import CartSerializer


class CartViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = CartSerializer
    queryset = Cart.objects.all()

    def get_queryset(self):
        user = self.request.user
        queryset = Cart.objects.filter(buyer__user=user)
        return queryset
