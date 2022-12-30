from rest_framework.permissions import BasePermission


class IsOwnerOrAdmin(BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        """
        Return True if permission is granted to the request user.
        """

        return obj.user == request.user or request.user.is_staff