from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from products.models import Category
from products.serializers import CategorySerializer


class ListCategoryView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
