from django.contrib.auth.models import User
from django.db import models
from django.db.models import Avg

class Books(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    
    @property
    def average_rating(self):
        return self.rating_set.aggregate(Avg('rating'))['rating__avg']

    def __str__(self):
            return self.title


class Rating(models.Model):
    rating = models.DecimalField(decimal_places=1, max_digits=3)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey('Books', on_delete=models.CASCADE)

    def __str__(self):
        return self.rating


class Shtetl(models.Model):
    game_played = models.DateTimeField(auto_now=True)
    winner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.winner
