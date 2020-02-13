from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from products.models import Product
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

    def create(self, request, *args, **kwargs):
        data = request.data
        products = data.get('products')
        data['buyer'] = request.user.buyer.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        for p in products:
            product = Product.objects.get(id=p.get('id'))
            order.products.add(product)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
