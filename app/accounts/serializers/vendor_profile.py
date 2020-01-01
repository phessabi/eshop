from rest_framework import serializers

from accounts.models import Vendor
from accounts.serializers import UserSerializer


class VendorProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Vendor
        fields = ('id', 'name', 'user')

