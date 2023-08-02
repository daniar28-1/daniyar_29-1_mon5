from django.db.models import Avg, Count
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

from movie_app.models import Director, Movie, Review
from rest_framework.decorators import api_view
from movie_app.serializers import (DirectorSerializer, MovieSerializer, ReviewSerializer,
MovieValidateserializer, ReviewValidateSerializer, DirectorValidateSerializer)


@api_view(['GET', 'POST'])
def list_director_api_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        data_dict = DirectorSerializer(directors, many=True).data
        directors_count = Director.objects.aggregate(directors=Count('director'))
        return Response(data=[data_dict, directors_count])
    elif request.method == 'POST':
        serializer = DirectorValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        name = serializer.validated_data.get('name')

        director = Director.objects.create(name=name)
        director.save()
        return Response(status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data='Director does not exist')
    if request.method == 'GET':
        data_dict = DirectorSerializer(director, many=False).data
        return Response(data_dict)
    elif request.method == 'DELETE':
        director.delete()
    elif request.method == 'PUT':
        serializer = DirectorValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        director.name = serializer.validated_data.get('name')
        director.save()
@api_view(['GET', 'PUT', 'DELETE'])
def moive_detail_api_view(request, id):
    try:
        moive = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data='Movie does not exist')
    if request.method == 'GET':
        data_dict = MovieSerializer(moive, many=False).data
        return Response(data_dict)
    elif request.method == 'DELETE':
        moive.delete()
    elif request.method == 'PUT':
        serializer = DirectorValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        moive.title = serializer.validated_data.get('title')
        moive.description = serializer.validated_data.get('description')
        moive.duration = serializer.validated_data.get('duration')
        moive.director_id = serializer.validated_data.get('director_id')
        moive.save()


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data='Movie does not exist')
    if request.method == 'GET':
        data_dict = MovieSerializer(review, many=False).data
        return Response(data_dict)
    elif request.method == 'DELETE':
        review.delete()
    elif request.method == 'PUT':
        serializer = DirectorValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        review.text = serializer.validated_data.get('text')
        review.stars = serializer.validated_data.get('stars')
        review.movie_id = serializer.validated_data.get('movie_id')

@api_view(['GET' 'POST'])
def list_Movie_api_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        data_dict = MovieSerializer(movies, many=True).data
        return Response(data_dict)
    if request.method == 'POST':
        serializer = MovieValidateserializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        duration = serializer.validated_data.get('duration')
        director_id = serializer.validated_data.get('director_id')

        movie = Movie.objects.create(title=title, description=description, duration=duration, director_id=director_id)
        movie.save()
        return Response(status=status.HTTP_201_CREATED)

@api_view(['GET' 'POST'])
def List_Review_api_view(request):
    if request.method == 'GET':
        rewievs = Review.objects.all()
        data_dict = ReviewSerializer(rewievs, many=True).data
        return Response(data_dict)
    if request.method == 'POST':
        serializer = ReviewValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        text = serializer.validated_data.get('text')
        stars = serializer.validated_data.get('stars')
        movie_id = serializer.validated_data.get('movie_id')

        review = Review.objects.create(text=text, stars=stars, movie_id=movie_id)

        review.save()
        return Response(status=status.HTTP_201_CREATED)



@api_view(['GET'])
def movies_reviews_api_view(request):
    movie_reviews = Review.objects.all()
    avg_stars = Review.objects.aggregate(avg=Avg('stars'))
    data_dict = ReviewSerializer(movie_reviews, many=True).data
    return Response(data=[data_dict, avg_stars])
