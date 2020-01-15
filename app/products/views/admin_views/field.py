from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from products.models import Field
from products.serializers import FieldSerializer


class AdminFieldViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, IsAdminUser)
    serializer_class = FieldSerializer
    queryset = Field.objects.all()
