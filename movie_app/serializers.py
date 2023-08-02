from movie_app.models import Director, Movie, Review
from rest_framework import serializers

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'name'.split()

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
