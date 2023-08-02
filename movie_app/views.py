from django.db.models import Avg, Count
from django.shortcuts import render
from rest_framework.response import Response

from movie_app.models import Director, Movie, Review
from rest_framework.decorators import api_view
from movie_app.serializers import DirectorSerializer, MovieSerializer, ReviewSerializer


@api_view(['GET'])
def list_director_api_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        data_dict = DirectorSerializer(directors, many=True).data
        directors_count = Director.objects.aggregate(directors=Count('director'))
        return Response(data_dict, directors_count)

@api_view(['GET'])
def director_detail_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data='Director does not exist')
    if request.method == 'GET':
        data_dict = DirectorSerializer(director, many=False).data
        return Response(data_dict)

@api_view(['GET'])
def list_Movie_api_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        data_dict = MovieSerializer(movies, many=True).data
        return Response(data_dict)

@api_view(['GET'])
def detail_movie_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
         Response(data='Movie does not exist')
    if request.method == 'GET':
        data_dict = MovieSerializer(movie, many=False).data
        return Response(data_dict)

@api_view(['GET'])
def List_Review_api_view(request):
    if request.method == 'GET':
        rewievs = Review.objects.all()
        data_dict = ReviewSerializer(rewievs, many=True).data
        return Response(data_dict)

@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data='Review does not exist')
    if request.method == 'GET':
        data_dict = ReviewSerializer(review, many=False).data
        return Response(data_dict)


@api_view(['GET'])
def movies_reviews_api_view(request):
    movie_reviews = Review.objects.all()
    avg_stars = Review.objects.aggregate(avg=Avg('stars'))
    data_dict = ReviewSerializer(movie_reviews, many=True).data
    return Response(data=[data_dict, avg_stars])
