from django.db import models


# Opções de nacionalidade para o modelo Actor
NATIONALITY_CHOICES = (("USA", "Estados Unidos"), ("BRAZIL", "Brasil"))


class Actor(models.Model):
    """
    Define o modelo para um ator.

    Este modelo representa um ator no sistema, incluindo seu nome, data de
    nascimento e nacionalidade.
    """

    # Nome do ator
    name = models.CharField(max_length=200, verbose_name="Nome")

    # Data de nascimento do ator
    birthday = models.DateField(
        null=True, blank=True, verbose_name="Data de Nascimento"
    )

    # Nacionalidade do ator
    nationality = models.CharField(
        max_length=100,
        choices=NATIONALITY_CHOICES,
        blank=True,
        null=True,
        verbose_name="Nacionalidade",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ator"
        verbose_name_plural = "Atores"
