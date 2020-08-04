from rest_framework import permissions


class IsCreatorOrReadOnly(permissions.BasePermission):
    """Allows POST/PUT/DELETE methods to creator only"""
    SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']

    def has_object_permission(self, request, view, obj):
        return (request.method in self.SAFE_METHODS or
                obj.creator.pk is request.user.pk)


class IsAdminOrReadOnly(permissions.BasePermission):
    """Allows POST/PUT/DELETE methods to admins only"""
    SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']

    def has_permission(self, request, view):
        return (request.method in self.SAFE_METHODS or
                request.user.is_staff)
