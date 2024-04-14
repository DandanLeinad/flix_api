from rest_framework import permissions


class ReviewPermissionClass(permissions.BasePermission):
    """Classe de permissão para avaliações."""

    # Verifica se o usuário tem permissão para realizar a ação
    def has_permission(self, request, view):

        # Verifica se o usuário tem permissão para visualizar avaliações
        if request.method in ["GET", "HEAD", "OPTIONS"]:
            return request.user.has_perm("reviews.view_review")

        # Verifica se o usuário tem permissão para adicionar uma nova avaliação
        if request.method == "POST":
            return request.user.has_perm("reviews.add_review")

        # Verifica se o usuário tem permissão para modificar uma avaliação existente
        if request.method in ["PUT", "PATCH"]:
            return request.user.has_perm("reviews.change_review")

        # Verifica se o usuário tem permissão para excluir uma avaliação existente
        if request.method == "DELETE":
            return request.user.has_perm("reviews.delete_review")

        # Retorna False se nenhuma verificação de permissão for bem-sucedida
        return False
