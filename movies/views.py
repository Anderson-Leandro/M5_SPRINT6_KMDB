from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAdminOrReadOnly
from .models import Movie
from .serializers import MovieSerializer

from genres.models import Genre


class MovieView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def perform_create(self, serializer):
        genres = self.request.data.pop("genres")
        genres_obj = []

        for genre in genres:
            retrive_genre = Genre.objects.filter(name=genre["name"]).first()
            if retrive_genre:
                genres_obj.append(retrive_genre)
            else:
                new_genre = Genre.objects.create(**genre)
                genres_obj.append(new_genre)

        serializer.save(user=self.request.user, genres=genres_obj)
