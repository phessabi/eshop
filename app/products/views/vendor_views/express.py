from rest_framework import status
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from _helpers.permissions import IsVendor
from products.models import Product
from products.serializers import ProductSerializer


class ExpressView(UpdateAPIView, GenericViewSet):
    permission_classes = (IsAuthenticated, IsVendor)
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def update(self, request, *args, **kwargs):
        vendor = request.user.vendor
        instance = self.get_object()
        if vendor.credit < instance.price * 0.10:
            return Response(status=status.HTTP_402_PAYMENT_REQUIRED)
        instance.express = True
        instance.save()
        return Response(status=status.HTTP_200_OK)
