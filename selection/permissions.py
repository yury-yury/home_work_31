from rest_framework.permissions import BasePermission

from selection.models import Selection


class SelectionEditPermission(BasePermission):
    """
    The SelectionEditPermission class inherits from the BasePermission class from the permissions module
    of the rest_framework library. Controls access to protected endpoints.
    """
    message: str = "Only owners, administrators, and moderators are allowed to edit the selection."

    def has_object_permission(self, request, view, obj: Selection) -> bool:
        """
        The has_object_permission function overrides the method of the base class. Accepts as arguments
        a request object, a view object, and a database object requested for editing.
        Checks the user's access rights to the requested actions. Returns True if the test result
        is positive, otherwise False.
        """
        if bool(request.user and (request.user.role in ["moderator", "admin"])):
            return True

        return obj.owner == request.user
