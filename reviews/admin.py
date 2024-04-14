from django.contrib import admin
from reviews.models import Review


# Registro do modelo Review no painel administrativo do Django
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Define como o modelo Review será exibido no painel de administração."""

    # Define quais campos serão exibidos na lista de avaliações
    list_display = ["id", "movie", "stars", "comment"]
