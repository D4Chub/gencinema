from django.urls import path

from api.v1.movies.views import MovieListView, GenreListView, PersonListView, MovieDetailView, MovieGenresView, PersonMovieView


urlpatterns = [
    path('movie/', MovieListView.as_view(), name="movie_list"),
    path('genre/', GenreListView.as_view(), name="genre_list"),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name="movie_detail"),
    path('actor/<int:actor_id>/movies/', PersonMovieView.as_view(), name="movies_by_actor"),
]