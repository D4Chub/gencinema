from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView

from .serializers import MovieSerializer, GenreSerializer, PersonSerializer
from apps.movies.models import Movie, Genre, Person

from drf_spectacular.utils import extend_schema


@extend_schema(
    responses=MovieSerializer,
    description="Список фильмов",
)
class MovieListView(ListAPIView):
    """
    Отображение списка всех(!) фильмов
    """

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
    """
    Отображение списка всех(!) жанров
    """

    model = Genre
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class PersonListView(ListAPIView):
    """
    Отображение списка всех персон (актеры, 
    режиссеры, сценаристы)
    """

    model = Person
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


@extend_schema(
    responses=MovieSerializer,
    description="Подробная информация о фильме",
)
class MovieDetailView(RetrieveAPIView):
    """
    Отображение фильма по id
    """

    model = Movie
    queryset = Movie.objects.filter(status=Movie.Status.PUBLISHED)
    serializer_class = MovieSerializer


@extend_schema(
    responses=MovieSerializer,
    description="Список фильмов по актеру",
)
class PersonMovieView(ListAPIView):
    """
    Отображение списка фильмов по конкретному актеру
    """

    serializer_class = MovieSerializer

    def get_queryset(self):
        actor_id = self.kwargs.get('actor_id')
        return Movie.objects.filter(personmovie__person_id=actor_id, personmovie__role=Person.Role.ACTOR)
