from rest_framework import filters
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from _helpers.throttles import SustainedAnonRateThrottle, BurstAnonRateThrottle
from products.models import Product, Category
from products.serializers import ProductSerializer


def list_all_products(category):
    categories = [category.id]
    if category.level == 3:
        return categories
    elif category.level == 2:
        cats3 = Category.objects.filter(parent_category=category)
        for c3 in cats3:
            categories.append(c3.id)
    elif category.level == 1:
        cats2 = Category.objects.filter(parent_category=category)
        for c2 in cats2:
            cats3 = Category.objects.filter(parent_category=c2)
            for c3 in cats3:
                categories.append(c3.id)
    return categories


class ListProductViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    permission_classes = (AllowAny,)
    throttle_classes = (BurstAnonRateThrottle, SustainedAnonRateThrottle,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    def get_queryset(self):
        category_id = self.request.query_params.get('category')
        sort_price = self.request.query_params.get('sort_price')
        queryset = Product.objects.all().order_by('-express')
        if category_id is not None:
            category = Category.objects.get(id=category_id)
            category_ids = list_all_products(category)
            queryset = Product.objects.filter(category_id__in=category_ids).order_by('-express')
        if sort_price is not None:
            if sort_price == 'ascending':
                queryset = queryset.order_by('-express', 'price_before_sale')
            else:
                queryset = queryset.order_by('-express', '-price')
        return queryset.filter(vendor__active=True)
