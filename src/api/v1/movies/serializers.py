from rest_framework import serializers

from apps.movies.models import Movie, Person, Genre


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'name', 'enName', 'role']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

    def to_representation(self, obj):
        return obj.name

class MovieSerializer(serializers.ModelSerializer):
    person = serializers.SerializerMethodField()
    genres = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = ['id',
                  'name',
                  'enName',
                  'description',
                  'year',
                  'madeIn',
                  'ageLimit',
                  'rating',
                  'movieLength',
                  'poster',
                  'premier',
                  'genres',
                  'person',
                  'status'
                ]
        read_only_fields = ['status']

    def get_person(self, obj):
        return PersonSerializer(obj.persons.all(), many=True).data
        

class MovieGenresSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = ['id', 'name', 'genres']


class MoviePersonsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ['id', 'name', 'person']

    def get_person(self, obj):
        return PersonSerializer(obj.persons.all(), many=True).data


class PersonMovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Person
        fields = ['id', 'name', 'movie']

    def get_movie(self, obj):
        return MovieSerializer(obj.movies.all(), many=True).data