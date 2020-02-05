from rest_framework import status
from rest_framework.generics import RetrieveAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from accounts.models import Buyer
from accounts.serializers import UserSerializer, BuyerProfileSerializer
from purchase.models import Cart


class CreateBuyerViewSet(GenericViewSet, CreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Buyer.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        cart = Cart.objects.create()
        Buyer.objects.create(user=user, name=data['name'], cart=cart)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UpdateRetrieveBuyerViewSet(GenericViewSet, UpdateAPIView, RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BuyerProfileSerializer
    queryset = Buyer.objects.all()

    def get_queryset(self):
        buyer = self.request.user.buyer
        return Buyer.objects.filter(id=buyer.id)

