from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsOwner(BasePermission):
    """Разрешения для хозяина профиля"""

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS and obj.user == request.user


class IsModerator(BasePermission):
    """Разрешения для user-moderator"""

    def has_permission(self, request, view):
        return request.user.role == 'moderator'


class IsAdminUser(BasePermission):
    """Разрешения для admin"""

    def has_permission(self, request, view):
        return request.user.role == 'admin'


class IsSuperUser(BasePermission):
    """Разрешения для superuser"""

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_superuser
