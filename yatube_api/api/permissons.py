from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrReadOnly(BasePermission):
    """
    Возвращает True, если автор поста является текущим
    пользователем
    """

    def has_object_permission(self, request, view, obj):
        return (
            request.method in SAFE_METHODS or
            request.user == obj.author
        )