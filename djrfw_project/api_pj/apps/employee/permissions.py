from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="admin").exists()


class IsEmployeeOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name="employee").exists():
            return obj.user == request.user
        return False
