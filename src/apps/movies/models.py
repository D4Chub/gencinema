from django.db import models


class Movie(models.Model):
    
    class Status(models.TextChoices):
        PUBLISHED = "published", "Опубликован"
        NOT_PUBLISHED = "not_published", "Не опубликован"
        DRAFT = "draft", "Черновик"
        DELETED = "deleted", "Удален"

    name = models.CharField(max_length=100, verbose_name="название")
    enName = models.CharField(max_length=100, verbose_name="англ название")
    description = models.TextField(verbose_name="описание")
    year = models.IntegerField(verbose_name="год")
    madeIn = models.CharField(max_length=100, verbose_name="страна")
    ageLimit = models.IntegerField(verbose_name="возрастное ограничение")
    rating = models.FloatField(verbose_name="рейтинг imdb")
    movieLength = models.IntegerField(verbose_name="длительность")
    poster = models.ImageField(upload_to="movies/", blank=True, null=True, verbose_name="постер")
    genres = models.ManyToManyField("Genre", verbose_name="жанры")
    premier = models.DateField(verbose_name="премьера")
    persons = models.ManyToManyField("Person", through='PersonMovie', related_name='movies', verbose_name="персоны")
    status = models.CharField(max_length=100, choices=Status.choices, default=Status.DRAFT, verbose_name="статус")

    class Meta:
        verbose_name = "фильм"
        verbose_name_plural = "фильмы"

    def __str__(self) -> str:
        return f"{self.name} ({self.year})"

class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name="название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "жанр"
        verbose_name_plural = "жанры"


class Person(models.Model):
    
    class Role(models.TextChoices):
        ACTOR = "actor", "актер"
        DIRECTOR = "director", "режиссер"
        WRITER = "writer", "сценарист"

    
    name = models.CharField(max_length=100, verbose_name="имя")
    enName = models.CharField(max_length=100, verbose_name="англ имя")
    role = models.CharField(max_length=100, verbose_name="роль", choices=Role.choices)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "персона"
        verbose_name_plural = "персоны"


class PersonMovie(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=Person.Role.choices)
