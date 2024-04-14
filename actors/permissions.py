from rest_framework import permissions


class ActorPermissionClass(permissions.BasePermission):
    """Classe de permissão para atores."""

    # Verifica se o usuário tem permissão para realizar a ação
    def has_permission(self, request, view):

        # Verifica se o usuário tem permissão para visualizar atores
        if request.method in ["GET", "HEAD", "OPTIONS"]:
            return request.user.has_perm("actors.view_actor")

        # Verifica se o usuário tem permissão para adicionar um novo ator
        if request.method == "POST":
            return request.user.has_perm("actors.add_actor")

        # Verifica se o usuário tem permissão para modificar um ator existente
        if request.method in ["PUT", "PATCH"]:
            return request.user.has_perm("actors.change_actor")

        # Verifica se o usuário tem permissão para excluir um ator existente
        if request.method == "DELETE":
            return request.user.has_perm("actors.delete_actor")

        # Retorna False se nenhuma verificação de permissão for bem-sucedida
        return False
