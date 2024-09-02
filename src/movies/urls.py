from django.urls import path

from .views import MovieListView, GenreListView, PersonListView


urlpatterns = [
    path('movies/', MovieListView.as_view()),
    path('genres/', GenreListView.as_view()),
    path('persons/', PersonListView.as_view()),
]