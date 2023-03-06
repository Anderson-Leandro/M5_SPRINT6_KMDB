from rest_framework import permissions


class IsAdminOrCritic(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "POST":
            if request.user.is_authenticated:
                return request.user.is_superuser or request.user.is_critic
            return False
        return True
