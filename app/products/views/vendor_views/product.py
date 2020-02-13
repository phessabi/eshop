from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from _helpers.permissions import IsVendor
from products.models import Product
from products.serializers import ProductSerializer


class VendorProductViewSet(ModelViewSet):
    authentication_classes = (JWTAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated, IsVendor)
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['vendor_id'] = self.request.user.vendor.id
        return context

    def get_queryset(self):
        vendor = self.request.user.vendor
        return Product.objects.filter(
            vendor=vendor,
            archived=False
        )

    def perform_destroy(self, instance: Product):
        instance.archived = True
        instance.save()
