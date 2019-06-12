from django.db import models


# Create your models here.
class Genre(models.Model):
    name = models.TextField()


class Movie(models.Model):
    title = models.TextField()
    audience = models.IntegerField()
    poster_url = models.IntegerField()
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)


class Score(models.Model):
    content = models.TextField()
    score = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
