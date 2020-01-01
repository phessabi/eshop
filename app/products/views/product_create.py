from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from _helpers.permissions import IsVendor
from products.models import Product
from products.serializers import ProductSerializer


class VendorProductViewSet(GenericViewSet, CreateAPIView, ListAPIView):
    permission_classes = (IsAuthenticated, IsVendor)
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_queryset(self):
        vendor = self.request.user.vendor
        return Product.objects.filter(vendor=vendor)

    def create(self, request, *args, **kwargs):
        data = request.data
        data['vendor'] = request.user.vendor.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

