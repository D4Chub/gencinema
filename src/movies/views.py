from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from rest_framework.generics import ListAPIView

from .serializers import MovieSerializer, GenreSerializer, PersonSerializer
from .models import Movie, Genre, Person

class MovieListView(ListAPIView):
    model = Movie
    queryset = Movie.objects.filter(status=Movie.Status.PUBLISHED)
    serializer_class = MovieSerializer


    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().get(request, *args, **kwargs)


class GenreListView(ListAPIView):
    model = Genre
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class PersonListView(ListAPIView):
    model = Person
    queryset = Person.objects.all()
    serializer_class = PersonSerializer