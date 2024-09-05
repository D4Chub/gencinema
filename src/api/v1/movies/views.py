from typing import Any
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.parsers import MultiPartParser

from .serializers import MovieSerializer, GenreSerializer, PersonSerializer
from apps.movies.models import Movie, Genre, Person
from drf_spectacular.utils import extend_schema


class MovieViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet):
    """
    Отображение списка всех(!) фильмов
    """

    model = Movie
    queryset = Movie.objects.filter(status=Movie.Status.PUBLISHED)
    serializer_class = MovieSerializer
    parser_classes = [MultiPartParser]


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


class PersonListView(RetrieveAPIView, CreateAPIView):
    """
    Отображение списка всех персон (актеры, 
    режиссеры, сценаристы)
    """

    model = Person
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    parser_classes = [MultiPartParser]


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
        try:
            actor_id = self.kwargs.get('actor_id')
            return Movie.objects.filter(personmovie__person_id=actor_id, personmovie__role=Person.Role.ACTOR)
        except ValueError:
            return JsonResponse({"message": "Actor id is not valid"}, status=400)
