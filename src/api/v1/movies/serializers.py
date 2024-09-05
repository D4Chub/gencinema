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


class MovieSerializer(serializers.ModelSerializer):
    persons= serializers.SerializerMethodField()
    genres = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = [
            'id', 
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
            'persons',
            'status'
            ]
        read_only_fields = ['status']

    def get_persons(self, obj):
        return PersonSerializer(obj.persons.all(), many=True).data
    
    def get_genres(self, obj):
        return GenreSerializer(obj.genres.all(), many=True).data
        

class MoviePersonsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ['id', 'name', 'person']

    def get_person(self, obj):
        return PersonSerializer(obj.persons.all(), many=True).data
