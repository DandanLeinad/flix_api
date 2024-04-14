from django.db import models
from movies.models import Movie
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    """
    Modelo que representa uma avaliação de um filme.

    Este modelo representa uma avaliação de um filme, contendo uma referência
    para o filme avaliado, a quantidade de estrelas dadas e um comentário
    opcional.
    """

    # Relacionamento com o modelo Movie
    movie = models.ForeignKey(
        Movie,
        on_delete=models.PROTECT,
        related_name="reviews",
        verbose_name="Filme",
    )

    # Quantidade de estrelas dadas
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, "Avaliação nao pode ser inferior a 0"),
            MaxValueValidator(5, "Avaliação não pode ser superior a 5"),
        ],
        verbose_name="Estrelas",
    )

    # Comentário opcional
    comment = models.TextField(
        null=True, blank=True, verbose_name="Comentário"
    )

    def __str__(self):
        return self.movie

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"
