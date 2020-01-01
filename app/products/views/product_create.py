from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from _helpers.permissions import IsVendor
from products.models import Product
from products.serializers import ProductSerializer


class ProductCreateViewSet(GenericViewSet, CreateAPIView, ListAPIView):
    permission_classes = (IsAuthenticated, IsVendor)
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_queryset(self):
        vendor = self.request.user.vendor
        return Product.objects.filter(vendor=vendor)
