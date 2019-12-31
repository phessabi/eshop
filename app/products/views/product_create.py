from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from _helpers.permissions import IsVendor
from products.serializers import ProductSerializer


class ProductCreateView(CreateAPIView):
    permission_classes = (IsAuthenticated, IsVendor)
    serializer_class = ProductSerializer
