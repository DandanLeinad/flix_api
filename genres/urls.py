from django.urls import path
from . import views


urlpatterns = [
    # URL para criar e listar gêneros
    path(
        "genres/",
        views.GenreCreateListView.as_view(),
        name="genre-create-list",
    ),
    # URL para detalhar, atualizar e excluir gêneros específicos
    path(
        "genres/<int:pk>/",
        views.GenreRetrieveUpdateDestroyView.as_view(),
        name="genre-detail",
    ),
]
