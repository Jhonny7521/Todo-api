from rest_framework import permissions

class CustomPermission(permissions.BasePermission):
  
  def has_permission(self, request, view):
    if request.user.is_superuser:
      return True
    if request.method in ['POST', 'GET']:
      return True

    return False