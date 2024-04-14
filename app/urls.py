from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # URL para acessar o painel de administração
    path("admin/", admin.site.urls),
    # URL para criar e listar gêneros
    path("api/v1/", include("genres.urls")),
    # URL para criar e listar atores
    path("api/v1/", include("actors.urls")),
    # URL para criar e listar filmes
    path("api/v1/", include("movies.urls")),
    # URL para criar e listar avaliações
    path("api/v1/", include("reviews.urls")),
    # URL para criar e listar usuários
    path("api/v1/", include("authentication.urls")),
]
