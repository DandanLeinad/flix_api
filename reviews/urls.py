from django.urls import path
from . import views


urlpatterns = [
    # URL para criar e listar avaliações
    path(
        "reviews/",
        views.ReviewCreateListView.as_view(),
        name="review-create-list",
    ),
    # URL para detalhar, atualizar e excluir avaliações específicas
    path(
        "reviews/<int:pk>/",
        views.ReviewRetrieveUpdateDestroyView.as_view(),
        name="review-detail",
    ),
]
