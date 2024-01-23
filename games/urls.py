from django.urls import path
from . import views

urlpatterns = [
    path("cards/", views.card_list, name="cards"),
    path("session/", views.game_session, name="session")
]