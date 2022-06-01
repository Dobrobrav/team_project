from rest_framework import serializers

from .models import Genres


class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = ["id", "name"]