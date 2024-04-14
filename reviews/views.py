from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from reviews.models import Review
from reviews.serializers import ReviewSerializer


class ReviewCreateListView(generics.ListCreateAPIView):
    """Endpoint para listar e criar avaliações."""

    permission_classes = (
        IsAuthenticated,
        GlobalDefaultPermission,
    )
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """Endpoint para recuperar, atualizar e deletar avaliações."""

    permission_classes = (
        IsAuthenticated,
        GlobalDefaultPermission,
    )
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
