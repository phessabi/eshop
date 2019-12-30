from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from products.models import Category
from products.serializers.category import CategorySerializer


class ListRetrieveFieldViewSet(GenericViewSet, ListAPIView, RetrieveAPIView):
    permission_classes = (AllowAny,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
