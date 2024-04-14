from django.apps import AppConfig


# Configuração para o aplicativo 'genres'.
class GenresConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "genres"
    verbose_name = "Gêneros"
