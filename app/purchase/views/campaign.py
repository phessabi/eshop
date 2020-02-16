from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from _helpers.permissions import IsVendor
from purchase.serializers import CampaignSerializer


class CampaignCreateAPIView(CreateAPIView):
    permission_classes = (IsAuthenticated, IsVendor)
    serializer_class = CampaignSerializer
