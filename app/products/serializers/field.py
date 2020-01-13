from rest_framework import serializers
from products.models import Field


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = ('id', 'name', 'category')
        read_only_fields = ('id', )
