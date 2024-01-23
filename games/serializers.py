from rest_framework import serializers
from .models import GameSession, Card

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameSession
        fields = ['id', 'host', 'players', 'cards', 'is_active']

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'name', 'description', 'is_active']