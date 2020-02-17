from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from _helpers.permissions import IsBuyer
from accounts.models import Buyer
from accounts.serializers import PhoneAddressSerializer


class PhoneAddressView(ListAPIView, GenericViewSet):
    permission_classes = (IsAuthenticated, IsBuyer)
    serializer_class = PhoneAddressSerializer
    queryset = Buyer.objects.all()

    def get_queryset(self):
        buyer = self.request.user.buyer
        queryset = Buyer.objects.filter(id=buyer.id)
        return queryset
