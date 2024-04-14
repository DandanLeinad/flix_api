from django.contrib import admin
from movies.models import Movie


# Registro do modelo Movie no painel de administração
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """Define como o modelo Movie será exibido no painel de administração."""

    # Define quais campos serão exibidos na lista de filmes
    list_display = ["id", "title", "genre", "release_date", "resume"]
