from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from products.models import Field
from products.serializers import FieldSerializer


class ListRetrieveFieldViewSet(GenericViewSet, ListAPIView, RetrieveAPIView):
    permission_classes = (AllowAny,)
    queryset = Field.objects.all()
    serializer_class = FieldSerializer
