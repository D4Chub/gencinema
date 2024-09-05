from django.urls import path
from rest_framework import routers

from api.v1.movies.views import MovieViewSet, GenreListView, PersonListView, MovieDetailView, PersonMovieView

routers = routers.DefaultRouter()
routers.register('movie', MovieViewSet, basename='movie')

urlpatterns = [
    path('genre/', GenreListView.as_view(), name="genre_list"),
    path('person/', PersonListView.as_view(), name="person_list"),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name="movie_detail"),
    path('actor/<int:actor_id>/movies/', PersonMovieView.as_view(), name="movies_by_actor"),

] + routers.urls