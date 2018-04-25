from rest_framework import permissions

class IsSelfOrReadOnly(permissions.BasePermission):
  def has_permission(self, request, view):
    return True

  def has_object_permission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
      return True

    return obj.id == request.user.id

class IsSystemAdmin(permissions.BasePermission):

  def has_permission(self, request, view):
    return request.user.role == 'admin'