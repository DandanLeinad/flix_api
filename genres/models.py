from django.db import models


class Genre(models.Model):
    """
    Define o modelo para um gênero.

    Este modelo representa um gênero no sistema, incluindo seu nome.
    """

    # Nome do gênero
    name = models.CharField(max_length=200, verbose_name="Nome")

    def __str__(self):
        return self.name
