from django.http import JsonResponse
from .models import GameSession, Card
from .serializers import GameSerializer, CardSerializer
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET', 'POST'])
def card_list(request):
    cards = Card.objects.all()
    serializer = CardSerializer(cards, many=True)
    return JsonResponse(serializer.data, safe=False)

def game_session(request):
    session = GameSession.objects.all()
    GameSerializer(session)