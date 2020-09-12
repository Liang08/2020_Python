from django.db import models


class Actor(models.Model):
    actor_name = models.CharField(max_length=30)
    actor_intro = models.TextField(max_length=1000, default='')
    actor_number = models.IntegerField(default=0)

    def __str__(self):
        return self.actor_name


class Movie(models.Model):
    film_name = models.CharField(max_length=30)
    film_number = models.IntegerField(default=0)
    film_intro = models.TextField(max_length=1000)
    film_year = models.CharField(max_length=10, default='')
    actor = models.ManyToManyField(Actor)

    def __str__(self):
        return self.film_name


class Comment(models.Model):
    comment = models.TextField(max_length=1000)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
