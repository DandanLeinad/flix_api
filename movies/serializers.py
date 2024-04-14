from rest_framework import serializers
from django.db.models import Avg
from movies.models import Movie
from actors.serializers import ActorSerializer
from genres.serializers import GenreSerializer


class MovieModelSerializer(serializers.ModelSerializer):
    """
    Serializador para o modelo Movie.

    Este serializador converte objetos do modelo Movie em representações JSON
    e vice-versa, facilitando a comunicação com a API.
    """

    # Campo calculado para a média das avaliações do filme
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = "__all__"

    # Método para calcular a média das avaliações do filme
    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg("stars"))["stars__avg"]

        if rate:
            return round(rate, 1)

        return None

    # Método para validar a data de lançamento do filme
    def validate_release_date(self, value):
        if value.year < 1990:
            raise serializers.ValidationError(
                "A data de lançamento não pode ser anterior a 1990."
            )
        return value

    # Método para validar o resumo do filme
    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError(
                "Resumo não deve ser maior que 200 caracteres."
            )
        return value


class MovieStatsSerializer(serializers.Serializer):
    """
    Serializador para estatísticas de filmes.

    Este serializador converte objetos de estatísticas de filmes em
    representações JSON e vice-versa, facilitando a comunicação com a API.
    """

    # Número total de filmes
    total_movies = serializers.IntegerField()

    # Número total de filmes por gênero
    movies_by_genre = serializers.ListField(
        child=serializers.DictField(
            child=serializers.CharField(), allow_empty=False
        )
    )

    # Número total de avaliações
    total_reviews = serializers.IntegerField()

    # Média das avaliações
    average_stars = serializers.FloatField()


class MovieListDetailSerializer(serializers.ModelSerializer):
    """Serializador para listar e detalhar filmes."""

    # Campo calculado para a média das avaliações do filme
    actors = ActorSerializer(many=True)
    genre = GenreSerializer()
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie

        # Campos a serem serializados
        fields = [
            "id",
            "title",
            "genre",
            "actors",
            "release_date",
            "rate",
            "resume",
        ]

    # Método para calcular a média das avaliações do filme
    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg("stars"))["stars__avg"]

        if rate:
            return round(rate, 1)

        return None
