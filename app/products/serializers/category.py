from rest_framework import serializers
from products.models import Category
from products.serializers.field import FieldSerializer


class CategorySerializer(serializers.ModelSerializer):
    fields = FieldSerializer(many=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'level', 'parent_category', 'fields')
        read_only_fields = ('id', 'fields')
