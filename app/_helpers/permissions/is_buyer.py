from rest_framework.permissions import BasePermission


class IsBuyer(BasePermission):

    def has_permission(self, request, view):
        user = request.user
        return user and hasattr(user, 'buyer') and user.buyer
