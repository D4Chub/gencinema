from django.urls import path

from api.v1.movies.views import MovieListView, GenreListView, PersonListView, MovieDetailView, MovieGenresView, PersonMovieView


urlpatterns = [
    path('movies/', MovieListView.as_view()),
    path('genres/', GenreListView.as_view()),
    path('persons/', PersonListView.as_view()),
    path('persons/<int:pk>/movies/', PersonMovieView.as_view()),
    path('movies/<int:pk>/detail/', MovieDetailView.as_view()),
    path('movies/<int:pk>/genres/', MovieGenresView.as_view()),
]