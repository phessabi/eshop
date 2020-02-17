from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from _helpers.permissions import IsVendor
from products.models import Product
from products.serializers import ProductSerializer, ImageSerializer


class VendorProductViewSet(ModelViewSet):
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


class ImageViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, IsVendor)
    serializer_class = ImageSerializer
    queryset = Product.objects.all()
    parser_classes = (MultiPartParser, FormParser,)

    def update(self, request, *args, **kwargs):
        print(request.data)
        instance = self.get_object()
        instance.image = self.request.data.get('image')
        instance.save()
        return Response(status=status.HTTP_200_OK)
