from django.urls import path
from . import views


urlpatterns = [
    # URL para criar e listar atores
    path(
        "actors/",
        views.ActorCreateListView.as_view(),
        name="actor-create-list",
    ),
    # URL para detalhes, atualização e exclusão de atores específicos
    path(
        "actors/<int:pk>/",
        views.ActorRetrieveUpdateDestroyView.as_view(),
        name="actor-detail",
    ),
]
