from rest_framework import permissions


class GenrePermissionClass(permissions.BasePermission):
    """Classe de permissão para gêneros."""

    # Verifica se o usuário tem permissão para realizar a ação
    def has_permission(self, request, view):

        # Verifica se o usuário tem permissão para visualizar gêneros
        if request.method in ["GET", "HEAD", "OPTIONS"]:
            return request.user.has_perm("genres.view_genre")

        # Verifica se o usuário tem permissão para adicionar um novo gênero
        if request.method == "POST":
            return request.user.has_perm("genres.add_genre")

        # Verifica se o usuário tem permissão para modificar um gênero existente
        if request.method in ["PUT", "PATCH"]:
            return request.user.has_perm("genres.change_genre")

        # Verifica se o usuário tem permissão para excluir um gênero existente
        if request.method == "DELETE":
            return request.user.has_perm("genres.delete_genre")

        # Retorna False se nenhuma verificação de permissão for bem-sucedida
        return False
