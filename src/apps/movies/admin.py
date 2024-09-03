from django.contrib import admin

from .models import Movie, Genre, Person

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("name", "year", "status")
    list_display_links = ("name",)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_display_links = ("name",)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("name", "role")
    list_display_links = ("name",)
