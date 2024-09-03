from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView

from .serializers import MovieGenresSerializer, MovieSerializer, GenreSerializer, PersonMovieSerializer, PersonSerializer
from apps.movies.models import Movie, Genre, Person

from drf_spectacular.utils import extend_schema, OpenApiParameter


@extend_schema(
    responses=MovieSerializer,
    description="Список фильмов",
)
class MovieListView(ListAPIView):
    model = Movie
    queryset = Movie.objects.filter(status=Movie.Status.PUBLISHED)
    serializer_class = MovieSerializer


    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().get(request, *args, **kwargs)

@extend_schema(
    responses=GenreSerializer,
    description="Список всех жанров",
)
class GenreListView(ListAPIView):
    model = Genre
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class PersonListView(ListAPIView):
    model = Person
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

@extend_schema(
    responses=MovieSerializer,
    description="Подробная информация о фильме",
)
class MovieDetailView(RetrieveAPIView):
    model = Movie
    queryset = Movie.objects.filter(status=Movie.Status.PUBLISHED)
    serializer_class = MovieSerializer

@extend_schema(
    responses=MovieSerializer,
    description="Жанры фильма",
)
class MovieGenresView(RetrieveAPIView):
    model = Movie
    queryset = Movie.objects.all()
    serializer_class = MovieGenresSerializer

@extend_schema(
    responses=MovieSerializer,
    description="Список фильмов по актеру",
)
class PersonMovieView(ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        actor_id = self.kwargs.get('actor_id')
        return Movie.objects.filter(personmovie__person_id=actor_id, personmovie__role=Person.Role.ACTOR)
