from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Games(models.Model):
    TYPE_OF_GAMES = [
        ("rank", "rank"),
        ("kill", "kill"),
        ("score", "score"),
        ("win", "win"),
    ]

    name = models.CharField(max_length=255, unique=True)
    type = models.CharField(choices=TYPE_OF_GAMES, max_length=255)

    def __str__(self):
        return f'{self.name} - {self.get_type_display()}'


class GamesOfUsers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, )
    games = models.ForeignKey(Games, on_delete=models.CASCADE, )
    score = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user} , {self.games} - {self.score}'
