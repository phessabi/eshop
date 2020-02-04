from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.viewsets import ModelViewSet

from purchase.models import Cart
from purchase.serializers.cart import CartSerializer


class CartViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
