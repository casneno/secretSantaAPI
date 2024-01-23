from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Card(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    is_active = models.BooleanField(default = False)

    def __str__(self):
        return self.name

class GameSession(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hosted_games')
    players = models.ManyToManyField(User, related_name='games')
    cards = models.ManyToManyField(Card, related_name='cards')
    is_active = models.BooleanField(default = False)