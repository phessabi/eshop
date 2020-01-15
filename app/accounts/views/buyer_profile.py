from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from accounts.models import Vendor
from accounts.serializers import UserSerializer, VendorProfileSerializer
from accounts.serializers import VendorSerializer


class CreateVendorViewSet(GenericViewSet, CreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Vendor.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        Vendor.objects.create(user=user, name=data['name'])
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ListRetrieveVendorViewSet(GenericViewSet, ListAPIView, RetrieveAPIView):
    permission_classes = (AllowAny,)
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class UpdateRetrieveVendorViewSet(GenericViewSet, UpdateAPIView, RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Vendor.objects.all()
    serializer_class = VendorProfileSerializer

    def get_queryset(self):
        vendor = self.request.user.vendor
        return Vendor.objects.filter(id=vendor.id)

