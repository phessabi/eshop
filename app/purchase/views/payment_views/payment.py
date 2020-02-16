from rest_framework.authentication import TokenAuthentication
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from _helpers.permissions import IsBuyer
from purchase.models import Payment
from purchase.serializers import PaymentSerializer


class PaymentView(ListModelMixin,
                  CreateModelMixin,
                  GenericViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsBuyer)
    serializer_class = PaymentSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Payment.objects.filter(buyer__user=user)
        return queryset
