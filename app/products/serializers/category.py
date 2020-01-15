from rest_framework import serializers
from products.models import Category
from products.serializers.field import FieldSerializer


class CategorySerializer(serializers.ModelSerializer):
    fields = FieldSerializer(many=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'level', 'parent_category', 'fields')
        read_only_fields = ('id', 'fields')
        extra_kwargs = {
            'parent_category': {'required': False}
        }

    def validate(self, attrs):
        data = self.context['request'].data
        # user = request.user
        # custom_user = CustomUser.objects.get(user=user)
        # user_groups = UserGroup.objects.filter(user=custom_user)
        # groups = [ug.group for ug in user_groups]
        # permissions = DBPermission.objects.filter(group__in=groups,
        #                                           db=attrs['db'],
        #                                           type='view')
        # if len(permissions) == 0:
        #     raise serializers.ValidationError("You do not have access to this DB")
        return attrs

