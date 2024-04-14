from rest_framework import permissions


class GlobalDefaultPermission(permissions.BasePermission):
    """
    Permissão global padrão.

    Esta permissão verifica se o usuário possui permissão para realizar uma
    determinada ação com base no modelo associado à visualização.
    """

    # Verifica se o usuário tem permissão para realizar a ação
    def has_permission(self, request, view):

        model_permission_codename = self.__get_model_permission_codename(
            method=request.method,
            view=view,
        )

        # Retorna False se não for possível obter o codinome da permissão do modelo
        if not model_permission_codename:
            return False

        # Retorna True se o usuário tiver a permissão necessária
        return request.user.has_perm(model_permission_codename)

    # Obtém o codinome da permissão do modelo com base no método HTTP
    def __get_model_permission_codename(self, method, view):

        try:
            model_name = view.queryset.model._meta.model_name
            app_label = view.queryset.model._meta.app_label
            action = self.__get_action_suffix(method)
            return f"{app_label}.{action}_{model_name}"

        except AttributeError:
            return None

    # Obtém o sufixo da ação com base no método HTTP
    def __get_action_suffix(self, method):

        method_actions = {
            "GET": "view",
            "POST": "add",
            "PUT": "change",
            "DELETE": "delete",
            "PATCH": "change",
            "OPTIONS": "view",
            "HEAD": "view",
        }

        return method_actions.get(method, "")
