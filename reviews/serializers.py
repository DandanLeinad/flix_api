from rest_framework import serializers
from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    """Serializador para o modelo Review."""

    class Meta:
        model = Review
        fields = "__all__"
