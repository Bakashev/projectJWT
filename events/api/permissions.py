from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminUserOrCreateOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method is not SAFE_METHODS:
            return True
        return bool(request.user.is_staff
                and request.method in SAFE_METHODS)