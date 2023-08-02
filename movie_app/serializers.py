from rest_framework.exceptions import ValidationError

from movie_app.models import Director, Movie, Review
from rest_framework import serializers


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=100)
    movie_id = serializers.IntegerField(min_value=1)
    stars = serializers.IntegerField()

    def validate_movie_id(self, movie_id):
        try:
            Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            return ValidationError('movie does not exist')
        return movie_id


class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)


class MovieValidateserializer(serializers.Serializer):
    title = serializers.CharField(max_length=20)
    description = serializers.CharField(max_length=100)
    duration = serializers.IntegerField()
    director_id = serializers.IntegerField(min_value=1)

    def validate_director_id(self, director_id):
        try:
            Director.objects.get(id=director_id)
        except Director.DoesNotExist:
            return ValidationError('Director does not exist')
        return director_id


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'name'.split()


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()

    class Meta:
        model = Review
        fields = '__all__'
