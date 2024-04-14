from django.urls import path
from . import views


urlpatterns = [
    # URL para criar e listar filmes
    path(
        "movies/",
        views.MovieCreateListView.as_view(),
        name="movie-create-list",
    ),
    # URL para detalhar, atualizar e excluir filmes específicos
    path(
        "movies/<int:pk>/",
        views.MovieRetrieveUpdateDestroyView.as_view(),
        name="movie-detail",
    ),
    # URL para obter estatísticas sobre os filmes
    path(
        "movies/stats",
        views.MovieStatsView.as_view(),
        name="movie-stats",
    ),
]
