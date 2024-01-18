from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class GameSession(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hosted_games')
    players = models.ManyToManyField(User, related_name='games')
    is_active = models.BooleanField(Default = False)

class Card(models.Model):
    game_session = models.ForeignKey(GameSession, on_delete=models.CASCADE, related_name='cards')
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    is_active = models.BooleanField(default = False)
