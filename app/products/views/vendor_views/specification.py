from rest_framework.mixins import CreateModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from _helpers.permissions import IsVendor
from products.serializers.specification import SpecificationSerializer


class VendorSpecificationViewSet(GenericViewSet, CreateModelMixin, UpdateModelMixin):
    permission_classes = (IsAuthenticated, IsVendor)
    serializer_class = SpecificationSerializer
