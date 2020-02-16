from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

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
