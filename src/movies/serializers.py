from rest_framework import serializers

from .models import Movie, Person, Genre


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

    def get_person(self, obj):
        return PersonSerializer(obj.persons.all(), many=True).data
