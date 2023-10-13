from rest_framework.permissions import BasePermission


class IsOwnerOrStaff(BasePermission):

    def has_permission(self, request, view):

        if request.user.is_staff:
            return True
        return view.queryset.filter(owner_id=request.user.id).exists()
