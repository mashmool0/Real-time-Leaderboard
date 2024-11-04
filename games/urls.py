from django.urls import path
from .views import AddGameUser

urlpatterns = [
    path('add/', AddGameUser.as_view(), name="add_to_game_user"),
]
