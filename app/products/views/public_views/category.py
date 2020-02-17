from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from _helpers.throttles import SustainedAnonRateThrottle, BurstAnonRateThrottle
from products.models import Category
from products.serializers import CategorySerializer


class ListCategoryView(GenericViewSet, ListModelMixin):
    permission_classes = (AllowAny,)
    throttle_classes = (BurstAnonRateThrottle, SustainedAnonRateThrottle,)
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
