from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from products.models import Category
from products.serializers import CategorySerializer


class ListCategoryView(GenericViewSet, ListModelMixin):
    permission_classes = (AllowAny,)
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
