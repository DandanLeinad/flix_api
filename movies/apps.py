from django.apps import AppConfig


# Configuração da aplicação de filmes
class MoviesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "movies"
    verbose_name = "Filmes"
