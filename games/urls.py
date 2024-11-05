from django.urls import path
from .views import AddGameUser

urlpatterns = [
    path('add/', AddGameUser.as_view(), name="add_to_game_user"),
    path('update/<str:game_name>', AddGameUser.as_view(), name="update_game_score"),
]
