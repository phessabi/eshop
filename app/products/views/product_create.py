from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from _helpers.permissions import IsVendor
from products.models import Product
from products.serializers import ProductSerializer


class ProductCreateView(GenericViewSet, CreateModelMixin, ListModelMixin):
    permission_classes = (IsAuthenticated, IsVendor)
    serializer_class = ProductSerializer

    def get_queryset(self):
        vendor = self.request.user.vendor
        return Product.objects.filter(vendor=vendor)
