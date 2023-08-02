from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=20)

class Movie(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    duration = models.IntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

class Review(models.Model):
    text = models.CharField(max_length=100)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)


