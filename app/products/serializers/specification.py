from rest_framework import serializers

from products.models import Specification


class SpecificationSerializer(serializers.ModelSerializer):
    field_name = serializers.SerializerMethodField()

    class Meta:
        model = Specification
        fields = ('id', 'product', 'field', 'field_name', 'value')
        read_only_field = ('id', 'field_name')

    @staticmethod
    def get_field_name(instance: Specification):
        return instance.field.name
