from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow authors of a recipe to edit or delete it.
    """

    def has_object_permission(self, request, view, obj):
        # 1. Read-only permissions are allowed for any request (GET, HEAD, OPTIONS)
        # These are called 'SAFE_METHODS'.
        if request.method in permissions.SAFE_METHODS:
            return True

        # 2. Write permissions (PUT, DELETE) are only allowed to the author of the recipe.
        # 'obj.author' refers to the user field we defined in our Recipe model.
        return obj.author == request.user