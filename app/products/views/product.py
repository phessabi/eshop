from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from products.models import Product
from products.serializers import ProductSerializer


class ListRetrieveProductViewSet(GenericViewSet, ListModelMixin):
    permission_classes = (AllowAny,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
