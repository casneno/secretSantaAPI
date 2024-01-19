from django.shortcuts import render, HttpResponse
from .models import Card

# Create your views here.
def home(request):
    return render(request, "home.html")

def session(request):
    cards = Card.objects.all()
    return render(request, "session.html", {"cards": cards})