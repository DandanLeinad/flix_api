from django.contrib import admin
from actors.models import Actor


# Registro do modelo Actor no painel de administração
@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    """
    Define como o modelo Actor será exibido no painel de administração.
    """

    # Define quais campos serão exibidos na lista de atores
    list_display = ("id", "name", "birthday", "nationality")
