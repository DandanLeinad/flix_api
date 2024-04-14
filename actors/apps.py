from django.apps import AppConfig


# Configuração para o aplicativo 'actors'.
class ActorsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "actors"
    verbose_name = "Atores"
