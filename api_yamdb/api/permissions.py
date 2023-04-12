from rest_framework import permissions


class AdminOnly(permissions.BasePermission):
    pass


class IsAdminUserOrReadOnly(permissions.BasePermission):
    pass


class AdminModeratorAuthorPermission(permissions.BasePermission):
    pass
