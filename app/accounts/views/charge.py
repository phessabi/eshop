from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from accounts.models import Charge
from accounts.serializers import ChargeSerializer


class ChargeView(ListCreateAPIView, GenericViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ChargeSerializer
    queryset = Charge.objects.all()

    def get_queryset(self):
        user = self.request.user
        queryset = Charge.objects.filter(user=user)
        return queryset

    def create(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        data['user'] = user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        charge = serializer.save()
        if hasattr(user, 'vendor'):
            user.vendor.credit += charge.amount
            user.vendor.save()
            user.save()
        else:
            user.buyer.credit += charge.amount
            user.buyer.save()
            user.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
