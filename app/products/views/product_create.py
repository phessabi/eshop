from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from _helpers.permissions import IsVendor
from products.models import Product
from products.serializers import ProductSerializer


class VendorProductViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, IsVendor)
    serializer_class = ProductSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['vendor'] = self.request.user.vendor.id
        return context

    def get_queryset(self):
        vendor = self.request.user.vendor
        return Product.objects.filter(
            vendor=vendor,
        )

    def perform_destroy(self, instance: Product):
        instance.archived = True
        instance.save()
