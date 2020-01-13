from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from products.serializers import CategorySerializer


class AdminCategoryViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, IsAdminUser)
    serializer_class = CategorySerializer
