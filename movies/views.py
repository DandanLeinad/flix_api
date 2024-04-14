from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count, Avg
from app.permissions import GlobalDefaultPermission
from movies.models import Movie
from reviews.models import Review
from movies.serializers import (
    MovieModelSerializer,
    MovieStatsSerializer,
    MovieListDetailSerializer,
)


class MovieCreateListView(generics.ListCreateAPIView):
    """Endpoint para listar e criar filmes."""

    permission_classes = (
        IsAuthenticated,
        GlobalDefaultPermission,
    )
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer

    # Sobrescrevendo o método get_serializer_class para retornar o serializador
    def get_serializer_class(self):
        if self.request.method == "GET":
            return MovieListDetailSerializer

        return MovieModelSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """Endpoint para detalhar, atualizar e excluir filmes específicos."""

    permission_classes = (
        IsAuthenticated,
        GlobalDefaultPermission,
    )
    queryset = Movie.objects.all()

    # Sobrescrevendo o método get_serializer_class para retornar o serializador
    def get_serializer_class(self):
        if self.request.method == "GET":
            return MovieListDetailSerializer

        return MovieModelSerializer


class MovieStatsView(views.APIView):
    """Endpoint para obter estatísticas sobre os filmes."""

    permission_classes = (
        IsAuthenticated,
        GlobalDefaultPermission,
    )
    queryset = Movie.objects.all()

    # Sobrescrevendo o método get para retornar as estatísticas
    def get(self, request):
        total_movies = self.queryset.count()
        movies_by_genre = self.queryset.values("genre__name").annotate(
            count=Count("id")
        )
        total_reviews = Review.objects.count()
        average_stars = Review.objects.aggregate(avg_stars=Avg("stars"))[
            "avg_stars"
        ]

        data = {
            "total_movies": total_movies,
            "movies_by_genre": movies_by_genre,
            "total_reviews": total_reviews,
            "average_stars": (round(average_stars, 1) if average_stars else 0),
        }

        serializer = MovieStatsSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        return response.Response(
            data=serializer.validated_data, status=status.HTTP_200_OK
        )
