from rest_framework import permissions


class MoviePermissionClass(permissions.BasePermission):
    """Classe de permissão para filmes."""

    # Verifica se o usuário tem permissão para realizar a ação
    def has_permission(self, request, view):

        # Verifica se o usuário tem permissão para visualizar filmes
        if request.method in ["GET", "HEAD", "OPTIONS"]:
            return request.user.has_perm("movies.view_movie")

        # Verifica se o usuário tem permissão para adicionar um novo filme
        if request.method == "POST":
            return request.user.has_perm("movies.add_movie")

        # Verifica se o usuário tem permissão para modificar um filme existente
        if request.method in ["PUT", "PATCH"]:
            return request.user.has_perm("movies.change_movie")

        # Verifica se o usuário tem permissão para excluir um filme existente
        if request.method == "DELETE":
            return request.user.has_perm("movies.delete_movie")

        # Retorna False se nenhuma verificação de permissão for bem-sucedida
        return False
