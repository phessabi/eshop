from rest_framework import status
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from _helpers.permissions import IsVendor
from purchase.models import Campaign
from purchase.serializers import CampaignSerializer


class CampaignViewSet(CreateModelMixin,
                      UpdateModelMixin,
                      DestroyModelMixin,
                      GenericViewSet):
    permission_classes = (IsAuthenticated, IsVendor)
    serializer_class = CampaignSerializer
    queryset = Campaign.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data
        data['start_datetime'] = data['start_datetime'].replace('T20:30:00.000Z', '')
        data['end_datetime'] = data['end_datetime'].replace('T20:30:00.000Z', '')
        data['sale_amount'] = data['sale_amount'] / 100
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

