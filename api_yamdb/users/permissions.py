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
        return bool(request.user and request.user.is_moderator)


# class IsAdmin(BasePermission):
#     """Разрешения для admin"""
#
#     def has_permission(self, request, view):
#         return bool(request.user and request.user.is_staff)


class IsSuperUser(BasePermission):
    """Разрешения для superuser"""

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)
