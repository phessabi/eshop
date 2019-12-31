from rest_framework.permissions import BasePermission


class IsVendor(BasePermission):

    def has_permission(self, request, view):
        user = getattr(request, 'user')
        return user and hasattr(user, 'vendor') and user.vendor
