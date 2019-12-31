from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.viewsets import GenericViewSet

from accounts.serializers.user import UserSerializer


class CreateUser(GenericViewSet, CreateAPIView):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ListRetrieveUser(GenericViewSet, ListAPIView, RetrieveAPIView):
    permission_classes = (IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
