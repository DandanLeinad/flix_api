from rest_framework import serializers
from actors.models import Actor


class ActorSerializer(serializers.ModelSerializer):
    """Serializador para o modelo Actor."""

    class Meta:
        model = Actor
        fields = "__all__"
