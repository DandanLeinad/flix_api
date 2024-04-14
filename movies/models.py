from django.db import models
from genres.models import Genre
from actors.models import Actor


class Movie(models.Model):
    """
    Define o modelo para um filme.

    Este modelo representa um filme no sistema, incluindo seu título, gênero,
    data de lançamento, atores e resumo.
    """

    # Título do filme
    title = models.CharField(max_length=500)

    # Gênero do filme
    genre = models.ForeignKey(
        Genre,
        on_delete=models.PROTECT,
        related_name="movies",
        verbose_name="Gênero",
    )

    # Data de lançamento do filme
    release_date = models.DateField(
        null=True, blank=True, verbose_name="Data de Lançamento"
    )

    # Atores do filme
    actors = models.ManyToManyField(
        Actor, related_name="movies", verbose_name="Atores"
    )

    # Resumo do filme
    resume = models.TextField(null=True, blank=True, verbose_name="Resumo")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Filme"
        verbose_name_plural = "Filmes"
