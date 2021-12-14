from django.contrib.auth.models import User
from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Allows access only to admin users.
    """
    def has_object_permission(self, request, view, obj):
        return obj == request.user