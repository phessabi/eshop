from rest_framework import serializers
from products.models import Specification


class SpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specification
        fields = ('field', 'value')
