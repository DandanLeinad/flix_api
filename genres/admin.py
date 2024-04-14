from django.contrib import admin
from genres.models import Genre


# Registro do modelo Genre no painel de administração
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """
    Define como o modelo Genre será exibido no painel de administração.
    """

    # Define quais campos serão exibidos na lista de gêneros
    list_display = ["id", "name"]
