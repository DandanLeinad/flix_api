from django.apps import AppConfig


# Configuração da aplicação reviews
class ReviewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reviews'
    verbose_name = 'Avaliações'
