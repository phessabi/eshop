from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from products.models import Product, Specification
from products.serializers.product import ProductSerializer
from products.serializers.specification import SpecificationSerializer


class ListRetrieveProductViewSet(GenericViewSet, ListAPIView, RetrieveAPIView):
    permission_classes = (AllowAny,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        product_serializer = self.get_serializer(instance)
        spec = Specification.objects.get(product=instance.id)
        spec_serializer = SpecificationSerializer(spec)
        data = {**product_serializer.data, **spec_serializer.data}
        return Response(data)

