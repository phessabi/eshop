from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from accounts.models import Vendor
from accounts.serializers.vendor import VendorSerializer


class CreateVendor(GenericViewSet, CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def create(self, request, *args, **kwargs):
        request.data['user'] = request.user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



class ListRetrieveVendor(GenericViewSet, ListAPIView, RetrieveAPIView):
    permission_classes = (AllowAny,)
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
