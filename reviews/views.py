from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from .models import Review
from .serializers import ReviewSerializer
from .permissions import IsAdminOrCritic

from movies.models import Movie
from users.models import User


class ReviewView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrCritic]

    lookup_url_kwarg = "movie_id"

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        movie_id = self.kwargs[self.lookup_url_kwarg]
        movie = get_object_or_404(Movie, id=movie_id)

        serializer.save(movie=movie, critic=self.request.user)
