from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):

    def has_permission(self, request, view):

        return view.queryset.filter(owner_id=request.user.id).exists()
