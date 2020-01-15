from rest_framework import serializers
from products.models import Category
from products.serializers.field import FieldSerializer


class CategorySerializer(serializers.ModelSerializer):
    fields = FieldSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'level', 'parent_category', 'fields')
        read_only_fields = ('id', 'fields')
        extra_kwargs = {
            'parent_category': {'required': False}
        }

    def validate(self, attrs):
        data = self.context['request'].data
        category_level = data.get('level')
        parent_category = data.get('parent_category')
        if category_level > 1 and parent_category is None:
            raise serializers.ValidationError("دسته‌های غیر سطح اول نیاز به دسته پدر دارند.")
        return attrs

