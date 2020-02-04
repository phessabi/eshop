from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from products.models import Product
from purchase.models import Cart
from purchase.serializers.cart import CartSerializer


class AddToCartView(GenericViewSet, CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CartSerializer
    queryset = Cart.objects.all()

    def create(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        product_id = data.get('id')
        product = Product.objects.get(id=product_id)
        user.buyer.cart.products.add(product)
        return Response(status=status.HTTP_200_OK)




