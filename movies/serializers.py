from rest_framework import serializers
from .models import Movie
from genres.serializers import GenreSerializer
from genres.models import Genre


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "duration",
            "premiere",
            "budget",
            "overview",
            "genres",
        ]
        extra_kwargs = {"genres": {"read_only": True}}

    def create(self, validated_data):
        genres = validated_data.pop("genres")
        instance = Movie.objects.create(**validated_data)
        instance.genres.set(genres)
        return instance
