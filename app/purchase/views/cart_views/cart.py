from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from products.models import Product
from purchase.models import Cart
from purchase.serializers import CartSerializer


class CartViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = CartSerializer
    queryset = Cart.objects.all()

    def get_queryset(self):
        user = self.request.user
        queryset = Cart.objects.filter(buyer__user=user)
        return queryset

    def destroy(self, request, *args, **kwargs):
        data = request.data
        product_id = data.get('id')
        product = Product.objects.get(id=product_id)
        instance = self.get_object()
        instance.products.remove(product)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        data = request.data
        product_id = data.get('id')
        product = Product.objects.get(id=product_id)
        instance = self.get_object()
        instance.products.add(product)
        return Response(status=status.HTTP_200_OK)


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
