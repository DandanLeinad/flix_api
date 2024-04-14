from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from genres.models import Genre
from genres.serializers import GenreSerializer


class GenreCreateListView(generics.ListCreateAPIView):
    """Endpoint para listar e criar gêneros."""

    permission_classes = (
        IsAuthenticated,
        GlobalDefaultPermission,
    )
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """Endpoint para detalhar, atualizar e excluir gêneros."""

    permission_classes = (
        IsAuthenticated,
        GlobalDefaultPermission,
    )
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
